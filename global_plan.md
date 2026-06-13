# Research Plan

## 1. Forward problem formulation and numerical simulation
- Formulation of the direct (forward) problem for a plane TE-polarized wave incident on a multilayer structure.
- Derivation of the governing equations from Maxwell’s equations.
- Numerical implementation of the forward problem in Python:
  - Transfer Matrix Method (TMM);
  - Direct solution via boundary-value formulation.
- Verification of the numerical model using limiting and benchmark cases.

## 2. Analysis of the reflection coefficient behavior
- Investigation of the dependence of the complex reflection coefficient
$$
r = r(k_i, h_i, \theta)
$$
on the physical parameters of the multilayer system.
- Analysis of resonance phenomena and interference effects.
- Sensitivity analysis with respect to layer thickness and refractive index.
- Identification of poorly conditioned parameter regions.

## 3. Classical inverse problem approaches
- Formulation of the inverse problem as a nonlinear least-squares minimization problem.
- Implementation of classical inversion methods:
  - Least Squares (LS);
  - Tikhonov regularization;
  - Levenberg–Marquardt (LM) algorithm.
- Study of stability, convergence, and sensitivity to noise.
- Comparison of reconstructed parameters with ground truth.

## 4. Feature extraction and representation of reflection data
- Analysis of the information content of the reflection coefficient.
- Construction of physically motivated features:
  - Reflectance $|r|^2$;
  - Spectral resonances and their spacing;
  - Integral and statistical spectral characteristics;
  - Phase and phase-derived quantities.
- Evaluation of feature robustness and informativeness for inverse modeling.

## 5. Machine learning models for parameter reconstruction
- Preparation of datasets based on synthetic simulations.
- Baseline machine learning models:
  - Linear and ridge regression;
  - Tree-based models.
- Integration of feature extraction into ML pipelines.
- Quantitative comparison with classical inverse methods.

## 6. Physics-Informed Neural Networks (PINNs)
- Overview of PINNs in the context of inverse wave problems.
- Formulation of physics-informed loss functions incorporating the forward model.
- Implementation of PINN-based inversion.
- Comparison of PINNs with classical and data-driven approaches.

## 7. Comparative analysis and evaluation
- Systematic comparison of all methods:
  - Accuracy of parameter reconstruction;
  - Stability with respect to noise;
  - Computational cost.
- Analysis of failure cases and ambiguities.
- Discussion of advantages and limitations of each approach.

## 8. Conclusions and future work
- Summary of obtained results.
- Implications for inverse wave problems in layered media.
- Possible extensions:
  - Multiple layers;
  - Noisy and incomplete data;
  - Experimental validation.