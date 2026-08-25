from typing import List, Tuple

try:
    import tensorflow as tf
except ImportError:
    tf = None

try:
    import torch
    import torch.nn as nn
except ImportError:
    torch = None
    nn = None


def build_tf_ann_model(
    input_dim: int,
    num_classes: int,
    hidden_units: Tuple[int, ...] = (128, 64),
    learning_rate: float = 0.001,
):
    """Builds and compiles a TensorFlow/Keras Artificial Neural Network for PMSM fault classification."""
    if tf is None:
        raise ImportError("TensorFlow is not installed. Please install tensorflow to use build_tf_ann_model.")

    layers = [tf.keras.layers.Input(shape=(input_dim,))]
    for units in hidden_units:
        layers.append(tf.keras.layers.Dense(units, activation="relu"))
        layers.append(tf.keras.layers.BatchNormalization())
        layers.append(tf.keras.layers.Dropout(0.1))

    # Output layer
    if num_classes > 2:
        layers.append(tf.keras.layers.Dense(num_classes, activation="softmax"))
        loss = "sparse_categorical_crossentropy"
    else:
        layers.append(tf.keras.layers.Dense(1, activation="sigmoid"))
        loss = "binary_crossentropy"

    model = tf.keras.models.Sequential(layers)
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss=loss, metrics=["accuracy"])
    return model


if torch is not None and nn is not None:
    class PyTorchANNModel(nn.Module):
        """PyTorch Deep Artificial Neural Network for PMSM Fault Classification."""

        def __init__(self, input_size: int, num_classes: int, hidden_units: List[int] = [128, 64, 32]):
            super().__init__()
            layers = []
            in_dim = input_size
            for h_dim in hidden_units:
                layers.append(nn.Linear(in_dim, h_dim))
                layers.append(nn.BatchNorm1d(h_dim))
                layers.append(nn.ReLU())
                layers.append(nn.Dropout(0.1))
                in_dim = h_dim

            layers.append(nn.Linear(in_dim, num_classes))
            self.network = nn.Sequential(*layers)

        def forward(self, x: torch.Tensor) -> torch.Tensor:
            return self.network(x)
else:
    class PyTorchANNModel:
        def __init__(self, *args, **kwargs):
            raise ImportError("PyTorch is not installed. Please install torch to use PyTorchANNModel.")
