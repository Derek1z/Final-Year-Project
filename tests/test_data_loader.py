from pathlib import Path
import pytest

try:
    import sklearn
except ImportError:
    sklearn = None

try:
    import torch
except ImportError:
    torch = None


def test_load_and_preprocess_data():
    if sklearn is None:
        pytest.skip("scikit-learn is not installed.")

    from src.data_loader import load_and_preprocess_data, PMSMDataset

    repo_root = Path(__file__).resolve().parent.parent
    data_path = repo_root / "data" / "Classification.csv"

    if not data_path.exists():
        pytest.skip("Dataset file Classification.csv not found for unit test.")

    data = load_and_preprocess_data(data_path=data_path)

    assert "X_train" in data
    assert "X_val" in data
    assert "X_test" in data
    assert "y_train" in data
    assert "y_val" in data
    assert "y_test" in data

    # Check feature shapes
    assert data["X_train"].shape[1] == 5  # Id, Iq, Vd, Vq, Wm
    assert len(data["classes"]) > 1

    if torch is not None:
        # Check PyTorch dataset wrapper
        ds = PMSMDataset(data["X_train"], data["y_train"])
        assert len(ds) == len(data["X_train"])
        feat, lbl = ds[0]
        assert isinstance(feat, torch.Tensor)
        assert isinstance(lbl, torch.Tensor)
