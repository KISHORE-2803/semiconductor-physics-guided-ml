"""Generate synthetic data from the documented reduced-order physics model."""
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from src.thermal_model import thermal_response
from src.thermo_mechanical_model import mismatch_strain, constrained_stress_indicator

ROOT = Path(__file__).resolve().parents[1]

def generate_dataset(n_samples=3000, seed=42):
    rng = np.random.default_rng(seed)
    # Ranges are exploratory bounds; see docs/03_assumptions_and_limitations.md.
    x = pd.DataFrame({
        "t_die_mm": rng.uniform(0.20, 0.80, n_samples),
        "t_underfill_mm": rng.uniform(0.05, 0.15, n_samples),
        "t_substrate_mm": rng.uniform(0.30, 1.00, n_samples),
        "k_die_W_mK": rng.uniform(100.0, 150.0, n_samples),
        "k_underfill_W_mK": rng.uniform(0.3, 2.0, n_samples),
        "k_substrate_W_mK": rng.uniform(0.5, 5.0, n_samples),
        "power_W": rng.uniform(1.0, 10.0, n_samples),
        "ambient_C": rng.uniform(25.0, 125.0, n_samples),
        "area_mm2": rng.uniform(25.0, 100.0, n_samples),
        "alpha_die_ppm_K": rng.uniform(2.5, 3.2, n_samples),
        "alpha_substrate_ppm_K": rng.uniform(10.0, 18.0, n_samples),
        "E_eff_GPa": rng.uniform(5.0, 25.0, n_samples),
        "nu_eff": rng.uniform(0.25, 0.40, n_samples),
    })
    targets = []
    for row in x.itertuples(index=False):
        tr = thermal_response(
            [row.t_die_mm * 1e-3, row.t_underfill_mm * 1e-3, row.t_substrate_mm * 1e-3],
            [row.k_die_W_mK, row.k_underfill_W_mK, row.k_substrate_W_mK],
            row.area_mm2 * 1e-6,
            row.power_W,
            row.ambient_C,
        )
        eps = mismatch_strain(
            row.alpha_die_ppm_K * 1e-6,
            row.alpha_substrate_ppm_K * 1e-6,
            tr["deltaT_K"],
        )
        sig = constrained_stress_indicator(eps, row.E_eff_GPa * 1e9, row.nu_eff)
        targets.append({
            **tr,
            "mismatch_strain": eps,
            "sigma_indicator_MPa": sig / 1e6,
        })
    return pd.concat([x, pd.DataFrame(targets)], axis=1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-samples", type=int, default=3000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=str, default=str(ROOT / "data" / "package_dataset.csv"))
    args = parser.parse_args()
    if args.n_samples < 10:
        raise SystemExit("--n-samples must be at least 10.")
    df = generate_dataset(args.n_samples, args.seed)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"Saved {len(df)} samples to {out}")
    print(df[["R_th_K_W", "deltaT_K", "T_die_C", "mismatch_strain", "sigma_indicator_MPa"]].describe())

if __name__ == "__main__":
    main()
