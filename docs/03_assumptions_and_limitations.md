# 03 — Assumptions, Parameterization and Limitations

## 1. Version 1 parameter ranges
The initial ranges below are exploratory modelling bounds, not Micron specifications and not universal material-property ranges. Before a physically defensible study is finalized, every material property range must be tied to a named material grade and a traceable source.

| Parameter | Symbol | Initial range | Unit |
|---|---:|---:|---|
| Die thickness | t_die | 0.20–0.80 | mm |
| Underfill thickness | t_uf | 0.05–0.15 | mm |
| Substrate thickness | t_sub | 0.30–1.00 | mm |
| Die thermal conductivity | k_die | 100–150 | W/(m K) |
| Underfill thermal conductivity | k_uf | 0.3–2.0 | W/(m K) |
| Substrate effective conductivity | k_sub | 0.5–5.0 | W/(m K) |
| Power dissipation | P | 1–10 | W |
| Ambient temperature | T_amb | 25–125 | °C |
| Effective heat-flow area | A | 25–100 | mm² |
| Die CTE | alpha_die | 2.5–3.2 | ppm/K |
| Substrate CTE | alpha_sub | 10–18 | ppm/K |
| Effective modulus | E_eff | 5–25 | GPa |
| Effective Poisson ratio | nu_eff | 0.25–0.40 | — |

The initial ranges are deliberately broad for sensitivity exploration. Do not describe them as measured values or as representative of a specific commercial package without checking authoritative material datasheets or literature.

## 2. Explicit assumptions
- Three-layer equivalent series stack.
- Constant thermal and elastic properties.
- Perfect bonding and thermal contact.
- Uniform effective area.
- Steady-state heat transfer.
- A single temperature rise is used in the first-order mismatch calculation.
- Fully constrained biaxial stress indicator.
- No residual stress, cure shrinkage, plasticity, creep, viscoelasticity or damage.

## 3. Known limitations
1. Real packages have parallel and three-dimensional heat paths.
2. Underfill may not form a simple full-area series layer in the actual package.
3. Silicon, underfill and substrate properties can depend on temperature and direction.
4. Interfaces and solder bumps alter heat transfer and mechanical constraint.
5. Local stresses concentrate near corners, bumps, vias and material interfaces.
6. The simplified stress indicator cannot identify failure location or failure mode.
7. Synthetic-data ML metrics measure agreement with the equations, not agreement with experiments.

## 4. Future extensions
- Replace equivalent series stack with a thermal resistance network including parallel paths and boundary resistances.
- Use temperature-dependent properties.
- Add copper/solder interconnects and realistic package geometry.
- Build a 2D/3D ANSYS or COMSOL model for comparison.
- Extract FEA-derived targets and train a surrogate on simulation data.
- Add uncertainty quantification and sensitivity analysis.

## 5. First-run numerical warning
The initial broad parameter sweep can produce very high estimated temperatures for combinations with low substrate conductivity, small effective area, high power and thick layers. These cases expose the limitations of treating the entire package as one series heat path. They must not be interpreted as realistic operating conditions. Before making engineering recommendations, narrow the design domain using traceable material/package data and improve the thermal network (for example, include parallel heat paths and boundary resistances), then compare against an independent FEA or measured reference.
