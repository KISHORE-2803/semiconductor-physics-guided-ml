# 01 — Project Charter

## 1. Problem statement
Semiconductor packages combine materials with dissimilar thermal conductivity, coefficient of thermal expansion (CTE), stiffness and geometry. Power dissipation produces temperature rise and gradients. Thermal expansion mismatch can create package deformation and stress, potentially contributing to reliability concerns.

A detailed package reliability assessment normally requires realistic geometry, boundary conditions, material constitutive behaviour, interfaces, manufacturing history and validation. Version 1 deliberately isolates a small set of physical relationships to create a transparent computational study.

## 2. Aim
Develop a reduced-order physics model and an ML surrogate that maps package design/operating inputs to thermal and first-order thermo-mechanical response indicators.

## 3. Research questions
1. How do layer thickness and thermal conductivity affect equivalent thermal resistance?
2. How do power dissipation and ambient temperature affect die temperature?
3. How does die-to-substrate CTE mismatch affect mismatch strain?
4. Can regression models reproduce outputs from the reduced-order physics model on unseen synthetic samples?
5. Which inputs dominate each predicted response, and are the trends physically plausible?

## 4. Objectives
- Derive and implement the thermal network equations.
- Derive and implement the first-order mismatch strain and constrained stress indicator.
- Generate a reproducible dataset from declared parameter ranges.
- Train and compare three regression algorithms.
- Evaluate with a held-out test set and residual/physical trend checks.
- Publish source code, documentation and reproducible results.

## 5. Deliverables
| ID | Deliverable | Acceptance evidence |
|---|---|---|
| D1 | Model definition | Equations, units and assumptions documented |
| D2 | Physics implementation | Functions return finite, dimensionally consistent outputs |
| D3 | Dataset | CSV with documented columns and fixed seed |
| D4 | Physics checks | Tests pass and expected monotonic trends hold |
| D5 | ML surrogate | Three models trained and evaluated on held-out data |
| D6 | Interpretation | Metrics, parity plots, residuals and feature importance |
| D7 | Reproducible repository | README and run instructions reproduce outputs |

## 6. Scope exclusions
Version 1 does not predict fatigue life, delamination, crack initiation, solder joint life, warpage fields or package failure probability. It does not use Micron proprietary data or claim validation against a commercial package.

## 7. Definition of success
Success means that the model is reproducible, its assumptions and limitations are explicit, physical sanity checks pass, and ML performance is reported honestly against the synthetic model. A high R² alone is not evidence of real-world package reliability prediction.
