import argparse
from pathlib import Path

import numpy as np

try:
    import tensorflow as tf
except ImportError:
    tf = None

try:
    import torch
    import torch.nn as nn
    from torch.utils.data import DataLoader
except ImportError:
    torch = None
    nn = None
    DataLoader = None

from .data_loader import PMSMDataset, load_and_preprocess_data
from .models import PyTorchANNModel, build_tf_ann_model


def train_tensorflow(data: dict, epochs: int, batch_size: int, output_dir: Path):
    """Trains a TensorFlow/Keras ANN model."""
    if tf is None:
        raise ImportError("TensorFlow is not installed. Cannot train TensorFlow model.")

    print("--- Training TensorFlow / Keras ANN Model ---")
    input_dim = data["X_train"].shape[1]
    num_classes = len(data["classes"])

    model = build_tf_ann_model(input_dim=input_dim, num_classes=num_classes)

    callbacks = [
        tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True),
        tf.keras.callbacks.ModelCheckpoint(
            filepath=str(output_dir / "best_model_tf.h5"),
            monitor="val_loss",
            save_best_only=True,
        ),
    ]

    history = model.fit(
        data["X_train"],
        data["y_train"],
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(data["X_val"], data["y_val"]),
        callbacks=callbacks,
        verbose=1,
    )

    test_loss, test_acc = model.evaluate(data["X_test"], data["y_test"], verbose=0)
    print(f"\n[TensorFlow] Test Accuracy: {test_acc * 100:.2f}% | Test Loss: {test_loss:.4f}")
    return model


def train_pytorch(data: dict, epochs: int, batch_size: int, output_dir: Path):
    """Trains a PyTorch ANN model."""
    if torch is None:
        raise ImportError("PyTorch is not installed. Cannot train PyTorch model.")

    print("--- Training PyTorch ANN Model ---")
    input_dim = data["X_train"].shape[1]
    num_classes = len(data["classes"])

    train_dataset = PMSMDataset(data["X_train"], data["y_train"])
    val_dataset = PMSMDataset(data["X_val"], data["y_val"])

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = PyTorchANNModel(input_size=input_dim, num_classes=num_classes).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    best_val_loss = float("inf")
    save_path = output_dir / "best_model_pt.pt"

    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for features, labels in train_loader:
            features, labels = features.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(features)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * features.size(0)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        train_loss = running_loss / total
        train_acc = correct / total

        # Validation
        model.eval()
        val_running_loss = 0.0
        val_correct = 0
        val_total = 0
        with torch.no_grad():
            for features, labels in val_loader:
                features, labels = features.to(device), labels.to(device)
                outputs = model(features)
                loss = criterion(outputs, labels)

                val_running_loss += loss.item() * features.size(0)
                _, predicted = torch.max(outputs, 1)
                val_total += labels.size(0)
                val_correct += (predicted == labels).sum().item()

        val_loss = val_running_loss / val_total
        val_acc = val_correct / val_total

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(model.state_dict(), save_path)

        if (epoch + 1) % 5 == 0 or epoch == epochs - 1:
            print(
                f"Epoch [{epoch+1:02d}/{epochs:02d}] "
                f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc*100:.2f}% | "
                f"Val Loss: {val_loss:.4f} | Val Acc: {val_acc*100:.2f}%"
            )

    print(f"\n[PyTorch] Saved best model state dict to: {save_path}")
    return model


def main():
    parser = argparse.ArgumentParser(description="Train PMSM Fault Classification Model")
    parser.add_argument("--data_path", type=str, default=None, help="Path to input CSV data")
    parser.add_argument("--epochs", type=int, default=35, help="Number of training epochs")
    parser.add_argument("--batch_size", type=int, default=64, help="Training batch size")
    parser.add_argument(
        "--framework",
        type=str,
        choices=["tensorflow", "pytorch", "both"],
        default="pytorch",
        help="Deep learning framework selection",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    output_dir = repo_root / "models"
    output_dir.mkdir(exist_ok=True)

    print("Loading PMSM dataset...")
    data = load_and_preprocess_data(data_path=args.data_path)
    print(f"Dataset loaded. Classes: {data['classes'].tolist()}")
    print(f"Features: {data['feature_names']}")

    if args.framework in ["tensorflow", "both"]:
        train_tensorflow(data, args.epochs, args.batch_size, output_dir)

    if args.framework in ["pytorch", "both"]:
        train_pytorch(data, args.epochs, args.batch_size, output_dir)


if __name__ == "__main__":
    main()
