# 06 — Validation and Reporting Protocol

## 1. Physics implementation checks
- Dimensional consistency for every equation.
- Positive thickness, conductivity, area and modulus.
- Poisson ratio in a physically admissible range for the chosen isotropic approximation.
- Finite outputs and no division by zero.
- Limiting-case and monotonic trend tests.

## 2. Dataset checks
- Record random seed and sample count.
- Check missing values, duplicate rows and finite outputs.
- Inspect min/max and distributions.
- Ensure samples remain inside declared parameter bounds.

## 3. Machine-learning evaluation
Use a held-out test set. Report separately for every target:
- R² (coefficient of determination)
- MAE (mean absolute error)
- RMSE (root mean squared error)

Do not report only the best model. Include the baseline Linear Regression result and compare all models on the same split.

## 4. Leakage prevention
- Split rows before fitting any learned preprocessing.
- Fit scalers/encoders on training data only.
- Do not use target-derived quantities as features when predicting those same targets.
- Do not tune repeatedly against the final test set. Use a validation split or cross-validation for tuning.

## 5. Interpretation checks
- Parity plot: predictions should lie near the 1:1 line.
- Residual plot: inspect bias and heteroscedasticity.
- Feature importance: interpret as model-specific association, not causality.
- Physical trend: probe controlled parameter sweeps and verify the surrogate does not violate obvious trends over the tested domain.

## 6. Claim discipline
A good score means the ML model approximates the synthetic physics model. It does not establish predictive accuracy for real packages. Real-world claims require independent FEA and/or experimental validation.

## 7. Operating-domain review
Inspect the generated temperature range before training or interpreting the ML model. Flag parameter combinations that produce temperatures outside the intended physical operating domain. Do not silently clip the outputs: either justify the domain, revise the thermal network/parameter bounds, or label the cases as numerical stress tests. The current broad initial sweep includes extreme estimates and requires this review before any real-package interpretation.
