# Comprehensive Literature Review

## Overview

This document summarizes key research papers and existing methodologies in the domain of Permanent Magnet Synchronous Motor (PMSM) fault diagnosis, classification, and signal processing.

---

### Paper 1: An Integrated Fault Detection and Identification System for PMSM in Electric Vehicles (2018)
- **Authors**: Ali Rohan, Mohammed Rabah, and Sung Ho Kim
- **Focus**: Integrated fault diagnosis architecture for electric vehicle traction motors operating under dynamic drive cycles.

---

### Paper 2: Fault Detection and Classification of PMSM in Variable Load and Speed Conditions Using Order Tracking and Machine Learning
- **Authors**: Jagath Sri Lal Senanayaka, Van Khang Huynh, Kjell G. Robbersmyr
- **Summary**:
  - **Problem Addressed**: Detecting and classifying faults in PMSMs operating under variable load and speed conditions (e.g. wind turbine applications).
  - **Aims**: Propose a fault diagnosis algorithm for detecting multiple faults under variable operating conditions by tracking frequency orders associated with faults using a normalized order spectrum, followed by machine learning classification.
  - **Methodology**:
    1. Estimate motor speed and torque using stator current measurements.
    2. Resample vibration/current signals to generate a normalized order spectrum.
    3. Extract fault-related frequency features.
    4. Employ Support Vector Machine (SVM) algorithms for fault classification.
  - **Merits & Impact**: High efficiency and reliability under dynamic speeds. Demonstrated efficacy on experimental test rigs.
  - **Limitations**: Primary testing focused on steady-state intervals under stepped speed profiles; future work extends to transient speed variations.

---

### Paper 3: Fault Diagnosis and Fault Frequency Determination of PMSM Using Deep Learning (2021)
- **Summary**:
  - **Approach**: 1D Convolutional Neural Network (CNN) for automatic feature extraction directly from motor current signals.
  - **Performance**: Achieved **98.85%** classification accuracy.
  - **Key Innovation**: Used weighted global average pooling and class feature maps to identify characteristic fault frequency components automatically without manual feature engineering.

---

### Paper 4: Stator Inter-Turn Short Circuit Fault Detection Using Neural Networks (2021)
- **Summary**:
  - **Approach**: Feed-forward neural network diagnostic tool utilizing statistical and spectral features extracted from three-phase stator current signals.
  - **Performance**: Achieved **93.125%** accuracy in detecting stator inter-turn faults across varying load levels and shorted turn counts.
  - **Context**: Stator inter-turn faults account for approximately **36%** of all industrial electric motor failures.

---

### Paper 5: Faults and Diagnosis Methods of Permanent Magnet Synchronous Motors: A Review (2018)
- **Taxonomy of PMSM Faults**:
  1. **Electrical Faults**: Stator winding inter-turn short circuits, open windings, phase-to-phase faults.
  2. **Mechanical Faults**: Bearing degradation, rotor shaft misalignment, static/dynamic air gap eccentricity.
  3. **Magnetic Faults**: Permanent magnet demagnetization (thermal, reverse field), rotor retaining ring / end-ring cracks.
- **Diagnostic Paradigms**:
  - *Model-Based*: Parameter estimation, parity equations, Luenberger/Kalman observers.
  - *Signal Processing*: Time-domain statistics, FFT spectral analysis, Hilbert-Huang Transform (HHT), Wavelet Transform (WT).
  - *Data-Driven / Machine Learning*: Support Vector Machines (SVM), Random Forest (RF), Artificial Neural Networks (ANN), Deep Convolutional Networks (1D-CNN).
