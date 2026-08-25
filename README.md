# PMSM Fault Detection & Classification using Neural Networks

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![TensorFlow 2.8+](https://img.shields.io/badge/TensorFlow-2.8%2B-orange.svg)](https://tensorflow.org/)
[![PyTorch 1.11+](https://img.shields.io/badge/PyTorch-1.11%2B-red.svg)](https://pytorch.org/)
[![MATLAB Simulink](https://img.shields.io/badge/MATLAB-Simulink-0076A8.svg)](https://www.mathworks.com/products/simulink.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An end-to-end engineering research repository for **Fault Detection and Multi-Class Classification in Permanent Magnet Synchronous Motors (PMSMs)** using Artificial Neural Networks (ANNs) built with TensorFlow/Keras and PyTorch, integrated with MATLAB/Simulink motor dynamic models.

---

## 📌 Project Overview

Permanent Magnet Synchronous Motors (PMSMs) are widely deployed in high-performance industrial applications, electric vehicle (EV) powertrains, and wind energy systems due to their high power density and efficiency. However, physical degradation, thermal overload, and mechanical stress can lead to electrical, mechanical, and magnetic faults.

This repository provides a complete machine learning and dynamic simulation framework to diagnose motor states using direct electrical telemetry signals ($I_d, I_q, V_d, V_q, W_m$).

### Key Features
- **Data Preprocessing & Scaling**: Robust feature standardization (`StandardScaler`), missing data handling, and label encoding (`LabelEncoder`).
- **Dual Framework Neural Networks**:
  - **TensorFlow / Keras ANN**: Multi-layer Dense Architecture with early stopping and checkpointing.
  - **PyTorch Deep ANN**: Custom `nn.Module` architecture with `DataLoader` integration.
- **Dynamic MATLAB/Simulink Models**: Full dynamic motor models (`.slx`, `.mdl`) and Simscape custom components (`.ssc`) for generating healthy and faulted motor telemetry under dynamic load conditions.
- **Modular Python CLI**: Command-line interfaces for training (`python -m src.train`) and evaluation (`python -m src.evaluate`).
- **Automated Unit Testing**: `pytest` test suite verifying data loaders and neural network forward passes.

---

## 🏗️ Repository Architecture

```
Final-Year-Project/
├── .gitignore                   # Ignores Python, MATLAB/Simulink cache, and OS files
├── LICENSE                      # MIT License
├── README.md                    # Project documentation & execution guide
├── requirements.txt             # Dependency specification
├── data/                        # Processed and raw telemetry datasets
│   ├── Classification.csv       # Multi-class fault dataset (7,511 records)
│   ├── Classification.xlsx
│   ├── Fault Detect.csv         # Binary fault detection dataset (7,506 records)
│   └── Fault Detect.xlsx
├── docs/                        # Research documentation & guides
│   ├── project_introduction.md  # Problem background & research objectives
│   ├── literature_review.md     # Comparative review of PMSM fault diagnosis literature
│   ├── pmsm_faults_guide.md     # Taxonomy of electrical, mechanical & magnetic faults
│   ├── presentation_notes.md    # Summary notes for presentation & project defense
│   └── references/              # Original reference documents & PPT template
│       ├── Introduction for project.docx
│       ├── Literature Reviews.docx
│       ├── Literature reviews for powerpoint.docx
│       ├── faults in pmsm and how to identify them.docx
│       └── knust-powerpoint-template.pptx
├── matlab_simulink/             # MATLAB & Simulink simulation models
│   ├── Faulted_PMSM_Example/    # Simscape faulted motor models (.slx, .ssc, .m)
│   ├── PMSM_Modeling/           # PMSM dynamic equations & parameter initialization
│   └── Simulation_Files/        # Standalone Simulink motor comparison models
├── models/                      # Saved pre-trained neural network models
│   └── best_model.h5            # Keras model checkpoint weights
├── notebooks/                   # Cleaned, reproducible Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_pmsm_fault_classification_tf.ipynb
│   └── 03_pmsm_fault_classification_pytorch.ipynb
├── src/                         # Core Python package
│   ├── __init__.py
│   ├── data_loader.py           # Data ingestion, scaling, and PyTorch dataset class
│   ├── models.py                # TensorFlow and PyTorch ANN model definitions
│   ├── train.py                 # CLI model training pipeline
│   └── evaluate.py              # CLI evaluation and classification report script
└── tests/                       # Unit tests
    ├── __init__.py
    ├── test_data_loader.py      # Tests dataset splits and tensor transformations
    └── test_models.py           # Tests neural network architecture shapes
```

---

## 📊 Dataset & Feature Specifications

The machine learning models ingest 5 key electrical and mechanical telemetry features:

| Feature Name | Symbol | Description | Unit |
| :--- | :--- | :--- | :--- |
| **Direct Current** | $I_d$ | $d$-axis stator current | Amperes (A) |
| **Quadrature Current** | $I_q$ | $q$-axis stator current (torque-producing) | Amperes (A) |
| **Direct Voltage** | $V_d$ | $d$-axis inverter output voltage | Volts (V) |
| **Quadrature Voltage** | $V_q$ | $q$-axis inverter output voltage | Volts (V) |
| **Rotor Speed** | $W_m$ | Mechanical angular speed | rad/s |

### Target Classes

1. **Class 0**: Healthy / Normal Operation
2. **Class 1**: Phase A Stator Fault
3. **Class 2**: Phase A & B Stator Fault
4. **Class 3**: Short Circuit Fault
5. **Class 4**: Open Circuit Fault

---

## 🚀 Quickstart & Usage

### 1. Installation

Clone the repository and install required dependencies:

```bash
git clone https://github.com/Derek1z/Final-Year-Project.git
cd Final-Year-Project
pip install -r requirements.txt
```

### 2. Training Models via CLI

Train a **TensorFlow/Keras** neural network model:
```bash
python -m src.train --framework tensorflow --epochs 35 --batch_size 64
```

Train a **PyTorch** neural network model:
```bash
python -m src.train --framework pytorch --epochs 30 --batch_size 64
```

Train both frameworks simultaneously:
```bash
python -m src.train --framework both
```

### 3. Model Evaluation

Evaluate a saved model against test data:
```bash
python -m src.evaluate --model_path models/best_model.h5
```

### 4. Running Unit Tests

Run the automated test suite using `pytest`:
```bash
pytest tests/
```

### 5. Interactive Notebooks

Launch Jupyter Notebook to explore data and train models interactively:
```bash
jupyter notebook notebooks/
```

---

## 🔬 MATLAB / Simulink Simulation

The `matlab_simulink/` directory contains dynamic motor models developed in MATLAB/Simulink:
- Open `matlab_simulink/Faulted_PMSM_Example/FaultedPMSM.slx` in MATLAB R2018b or newer to run time-domain fault injection simulations.
- Run `FaultedPMSMParameters.m` to load motor parameters into the MATLAB workspace prior to running Simulink models.

---

## 📄 Documentation

Comprehensive documentation converted to Markdown is available in the `docs/` folder:
- [`docs/project_introduction.md`](docs/project_introduction.md) - Background, problem statement, and objectives.
- [`docs/literature_review.md`](docs/literature_review.md) - Review of 5 landmark research papers in PMSM fault diagnosis.
- [`docs/pmsm_faults_guide.md`](docs/pmsm_faults_guide.md) - Diagnostic guide for electrical, mechanical, and magnetic faults.
- [`docs/presentation_notes.md`](docs/presentation_notes.md) - Key slides overview and presentation defense notes.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🎓 Citation & Acknowledgments

Developed as part of the **Final Year Engineering Project** at **Kwame Nkrumah University of Science and Technology (KNUST)**.
