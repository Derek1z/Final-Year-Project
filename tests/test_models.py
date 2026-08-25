import numpy as np
import pytest
from src.models import build_tf_ann_model, PyTorchANNModel

try:
    import tensorflow as tf
except ImportError:
    tf = None

try:
    import torch
except ImportError:
    torch = None


def test_tf_ann_model_forward():
    if tf is None:
        pytest.skip("TensorFlow is not installed.")
    model = build_tf_ann_model(input_dim=5, num_classes=5)
    dummy_input = np.random.randn(10, 5).astype(np.float32)
    output = model.predict(dummy_input, verbose=0)
    assert output.shape == (10, 5)
    np.testing.assert_allclose(np.sum(output, axis=1), 1.0, rtol=1e-5)


def test_pytorch_ann_model_forward():
    if torch is None:
        pytest.skip("PyTorch is not installed.")
    model = PyTorchANNModel(input_size=5, num_classes=5)
    dummy_input = torch.randn(10, 5)
    output = model(dummy_input)
    assert output.shape == (10, 5)
