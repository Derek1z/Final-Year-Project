import os
from pathlib import Path
from typing import Dict, Optional, Tuple, Union

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import torch
from torch.utils.data import Dataset


class PMSMDataset(Dataset):
    """PyTorch Dataset wrapper for PMSM electrical telemetry feature tensors."""

    def __init__(self, features: np.ndarray, labels: np.ndarray):
        self.features = torch.tensor(features, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self) -> int:
        return len(self.features)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        return self.features[idx], self.labels[idx]


def load_and_preprocess_data(
    data_path: Optional[Union[str, Path]] = None,
    target_column: str = "Output",
    test_size: float = 0.2,
    val_size: float = 0.5,
    random_state: int = 42,
) -> Dict[str, Union[np.ndarray, StandardScaler, LabelEncoder, list]]:
    """Loads and preprocesses PMSM telemetry dataset.

    Parameters
    ----------
    data_path : str or Path, optional
        Path to CSV file. Defaults to `data/Classification.csv` relative to repo root.
    target_column : str
        Name of target column (e.g. 'Output').
    test_size : float
        Fraction of data reserved for temporary test/val split.
    val_size : float
        Fraction of temporary data reserved for validation.
    random_state : int
        Seed for train/test splits.

    Returns
    -------
    dict
        Dictionary containing preprocessed arrays (X_train, X_val, X_test, y_train, y_val, y_test),
        fitted `scaler`, fitted `label_encoder`, and feature name list.
    """
    if data_path is None:
        base_dir = Path(__file__).resolve().parent.parent
        data_path = base_dir / "data" / "Classification.csv"
    else:
        data_path = Path(data_path)

    if not data_path.exists():
        raise FileNotFoundError(f"Dataset file not found at: {data_path}")

    # Load dataset
    raw_df = pd.read_csv(data_path)

    # Clean unnamed columns
    clean_df = raw_df.loc[:, ~raw_df.columns.str.contains("^Unnamed")].copy()

    if target_column not in clean_df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataset columns: {clean_df.columns.tolist()}")

    # Separate features and target
    X = clean_df.drop(columns=[target_column])
    y = clean_df[target_column]
    feature_names = X.columns.tolist()

    # Train / Val / Test split
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=val_size, random_state=random_state, stratify=y_temp
    )

    # Standardize numerical features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)

    # Encode label classes
    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(y_train)
    y_val_encoded = label_encoder.transform(y_val)
    y_test_encoded = label_encoder.transform(y_test)

    return {
        "X_train": X_train_scaled,
        "X_val": X_val_scaled,
        "X_test": X_test_scaled,
        "y_train": y_train_encoded,
        "y_val": y_val_encoded,
        "y_test": y_test_encoded,
        "scaler": scaler,
        "label_encoder": label_encoder,
        "feature_names": feature_names,
        "classes": label_encoder.classes_,
    }
