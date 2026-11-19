# 05 — Data Dictionary

The dataset is synthetic and generated from `src/` physics functions.

## Input columns
| Column | Description | Unit |
|---|---|---|
| `t_die_mm` | Silicon die thickness | mm |
| `t_underfill_mm` | Underfill thickness | mm |
| `t_substrate_mm` | Substrate thickness | mm |
| `k_die_W_mK` | Die thermal conductivity | W/(m K) |
| `k_underfill_W_mK` | Underfill thermal conductivity | W/(m K) |
| `k_substrate_W_mK` | Effective substrate thermal conductivity | W/(m K) |
| `power_W` | Applied heat/power | W |
| `ambient_C` | Ambient temperature | °C |
| `area_mm2` | Effective heat-flow area | mm² |
| `alpha_die_ppm_K` | Die CTE | ppm/K |
| `alpha_substrate_ppm_K` | Substrate CTE | ppm/K |
| `E_eff_GPa` | Effective modulus for stress indicator | GPa |
| `nu_eff` | Effective Poisson ratio | — |

## Target columns
| Column | Description | Unit |
|---|---|---|
| `R_th_K_W` | Equivalent series thermal resistance | K/W |
| `deltaT_K` | Temperature rise across equivalent stack | K |
| `T_die_C` | Estimated die temperature | °C |
| `mismatch_strain` | Magnitude of first-order CTE mismatch strain | — |
| `sigma_indicator_MPa` | Fully constrained biaxial stress indicator | MPa |

## Provenance
No experimental data are used. Every target is computed from the equations in `docs/02_physics_and_equations.md`. The dataset must never be described as measured package data.
