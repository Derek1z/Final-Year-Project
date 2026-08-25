# Project Presentation Notes & Literature Digest

Key summaries prepared for final year presentation slides and defense:

---

## 1. Digital Twin & ISSA-Random Forest (2022)
- **Concept**: Digital Twin combined with Improved Sparrow Search Algorithm (ISSA) optimized Random Forest for PMSM fault diagnosis.
- **Key Method**: Sampled training subsets, extracted statistical features, optimized decision trees using ISSA.
- **Takeaway**: Showed high classification accuracy in coal mine belt conveyor applications.

## 2. Order Tracking & Support Vector Machines
- **Concept**: Order spectrum normalization for variable speed/load motors.
- **Key Method**: Tracked frequency orders to eliminate speed fluctuation smearing.
- **Takeaway**: SVM classifiers achieved high accuracy across variable operating speeds.

## 3. 1D-Convolutional Neural Networks (2021)
- **Concept**: End-to-end deep feature learning directly from raw current waveforms.
- **Key Method**: Weighted global average pooling eliminates manual feature extraction.
- **Takeaway**: Reached 98.85% accuracy on benchmark motor datasets.

## 4. Artificial Neural Network (ANN) Proposed Solution
- **Input Telemetry**: Stator $d$-$q$ currents ($I_d, I_q$), voltages ($V_d, V_q$), and rotor speed ($W_m$).
- **Model Architecture**: Multi-layer Dense Neural Network with ReLU activations, BatchNorm, and Softmax classification.
- **Target Classes**:
  - Class 0: Healthy / Normal
  - Class 1: Phase A Stator Fault
  - Class 2: Phase A & B Stator Fault
  - Class 3: Short Circuit Fault
  - Class 4: Open Circuit Fault
