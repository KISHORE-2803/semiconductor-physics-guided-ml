# 02 — Physics Model and Equations

## 1. Geometry abstraction
Version 1 represents the package as three equivalent layers in series along a one-dimensional heat-flow path:
1. Silicon die
2. Underfill
3. Substrate

This is an equivalent reduced-order stack, not a geometric reconstruction of a flip-chip package. The selected area `A` is the effective cross-sectional area normal to the assumed heat-flow direction.

## 2. Steady one-dimensional thermal network
For layer `i`, with thickness `t_i` [m], conductivity `k_i` [W/(m K)] and effective area `A` [m²]:

`R_i = t_i / (k_i A)` [K/W]

For layers in series:

`R_th = sum_i R_i` [K/W]

For applied heat/power `P` [W]:

`DeltaT = P R_th` [K]

`T_die = T_ambient + DeltaT` [K]

The temperature rise is identical numerically in kelvin and degrees Celsius. The absolute temperature is reported in kelvin internally and degrees Celsius in the dataset for readability.

## 3. Thermal assumptions
- Steady state.
- One-dimensional heat flow.
- Constant properties.
- Perfect thermal contact between layers.
- No convection/radiation branch or lateral heat spreading.
- All dissipated power crosses the equivalent series stack.
- No explicit package-to-board or heat-sink boundary network.

## 4. CTE mismatch
For a first-order free thermal expansion estimate, the relative in-plane mismatch strain between die and substrate is:

`epsilon_mis = (alpha_die - alpha_substrate) * DeltaT`

where CTE is in [1/K]. The sign indicates which material expands more; the magnitude is used for the stress indicator.

## 5. Constrained biaxial stress indicator
Under an idealized, fully constrained, isotropic plane-stress approximation:

`sigma_indicator = E_eff / (1 - nu_eff) * abs(epsilon_mis)`

where `E_eff` [Pa] and `nu_eff` [-] are declared effective properties. Version 1 uses a documented effective modulus/Poisson ratio as a proxy, not a solved multilayer elasticity problem.

The quantity is an order-of-magnitude indicator only. It is not the local die corner stress, interfacial peel/shear stress, a fracture parameter, or a failure criterion.

## 6. Units
| Quantity | Symbol | SI unit |
|---|---|---|
| Layer thickness | t | m |
| Thermal conductivity | k | W/(m K) |
| Effective area | A | m² |
| Thermal resistance | R_th | K/W |
| Power | P | W |
| Temperature | T | K or °C |
| CTE | alpha | 1/K |
| Strain | epsilon | dimensionless |
| Young's modulus | E | Pa |
| Poisson ratio | nu | dimensionless |
| Stress indicator | sigma | Pa |

## 7. Important modelling distinction
The ML model is trained to reproduce outputs of this reduced-order physics model. It is therefore a surrogate of the chosen equations, not a model trained on measured semiconductor package performance.
