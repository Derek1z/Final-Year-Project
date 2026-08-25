# PMSM Faults Taxonomy & Diagnostic Identification Guide

Permanent Magnet Synchronous Motors (PMSMs) exhibit high power density and efficiency, but operational stress can induce specific physical faults. This guide outlines common PMSM fault modes, root causes, and diagnostic identification signatures.

---

## 1. Electrical Faults

### Stator Winding Inter-Turn Faults
- **Cause**: Breakdown of turn-to-turn wire insulation due to excessive thermal stress, voltage surges, mechanical vibration, or chemical aging.
- **Identification**:
  - Unbalance in three-phase stator currents ($I_a, I_b, I_c$).
  - Emergence of specific harmonic sidebands around fundamental supply frequencies ($f_s \pm k \cdot f_r$).
  - Temperature rise around localized stator slots.

### Open Circuit Winding Faults
- **Cause**: Mechanical fracture of phase conductors, terminal connection loosening, or inverter switch open-circuit failures.
- **Identification**:
  - Complete zero current on the affected phase.
  - Significant torque ripple and output power drop.
  - High negative-sequence current component.

---

## 2. Mechanical Faults

### Bearing Degradation & Failures
- **Cause**: Inadequate lubrication, mechanical overload, contamination, or shaft currents passing through bearing balls.
- **Identification**:
  - High-frequency vibration components at characteristic bearing defect frequencies (BPFO, BPFI, BSF, FTF).
  - Acoustic noise increase.

### Shaft Misalignment & Rotor Eccentricity
- **Cause**: Incorrect coupling alignment, foundation distortion, bent shaft, or rotor bearing wear causing uneven air gap distance between rotor and stator.
- **Identification**:
  - Unbalanced Magnetic Pull (UMP) inducing $1\times$ and $2\times$ rotational frequency vibrations.
  - Fluctuations in $d$-axis and $q$-axis flux linkages.

---

## 3. Magnetic Faults

### Permanent Magnet Demagnetization
- **Cause**: Thermal overload exceeding Curie temperature, strong armature reaction magnetic fields during short circuits, or physical magnet cracking.
- **Identification**:
  - Reduction in back-EMF amplitude.
  - Increase in stator current required to produce equivalent electromagnetic torque.
  - Distortions in $I_d, I_q$ current response under vector control.

---

## 4. Key Diagnostic Signals for ML / ANN Classifiers

| Parameter | Symbol | Diagnostic Role |
| :--- | :--- | :--- |
| **Direct Current** | $I_d$ | Sensitive to magnet flux changes and flux-weakening conditions |
| **Quadrature Current** | $I_q$ | Directly proportional to electromagnetic torque output |
| **Direct Voltage** | $V_d$ | Inverter output voltage vector $d$-component |
| **Quadrature Voltage**| $V_q$ | Inverter output voltage vector $q$-component |
| **Mechanical Speed** | $W_m$ | Rotor angular velocity, reflects load-speed variations |
