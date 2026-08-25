import argparse
from pathlib import Path

import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

try:
    import tensorflow as tf
except ImportError:
    tf = None

from .data_loader import load_and_preprocess_data


def evaluate_model(model_path: Path, data_path: Path = None):
    """Evaluates trained TensorFlow/Keras model on the test split."""
    if tf is None:
        raise ImportError("TensorFlow is not installed. Cannot evaluate TensorFlow model.")

    print(f"Loading data and model from: {model_path}")
    data = load_and_preprocess_data(data_path=data_path)

    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")

    model = tf.keras.models.load_model(model_path)

    y_pred_probs = model.predict(data["X_test"])
    if y_pred_probs.ndim > 1 and y_pred_probs.shape[1] > 1:
        y_pred = np.argmax(y_pred_probs, axis=1)
    else:
        y_pred = (y_pred_probs > 0.5).astype(int).flatten()

    y_true = data["y_test"]
    class_names = [str(c) for c in data["classes"]]

    acc = accuracy_score(y_true, y_pred)
    print("\n==========================================")
    print(f" PMSM Fault Classification Evaluation")
    print("==========================================")
    print(f"Overall Accuracy: {acc * 100:.2f}%\n")
    print("Classification Report:")
    print(classification_report(y_true, y_pred, target_names=class_names, zero_division=0))

    cm = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:")
    print(cm)
    print("==========================================")


def main():
    parser = argparse.ArgumentParser(description="Evaluate PMSM Fault Classification Model")
    parser.add_argument("--model_path", type=str, default=None, help="Path to saved model file (.h5)")
    parser.add_argument("--data_path", type=str, default=None, help="Path to test CSV data")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    model_path = Path(args.model_path) if args.model_path else repo_root / "models" / "best_model.h5"

    evaluate_model(model_path=model_path, data_path=args.data_path)


if __name__ == "__main__":
    main()
