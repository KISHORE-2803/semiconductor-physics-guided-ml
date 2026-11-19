"""Train baseline regression surrogates and save metrics/plots."""
from __future__ import annotations

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

ROOT = Path(__file__).resolve().parents[1]
FEATURES = [
    "t_die_mm", "t_underfill_mm", "t_substrate_mm",
    "k_die_W_mK", "k_underfill_W_mK", "k_substrate_W_mK",
    "power_W", "ambient_C", "area_mm2",
    "alpha_die_ppm_K", "alpha_substrate_ppm_K", "E_eff_GPa", "nu_eff",
]
TARGETS = ["R_th_K_W", "deltaT_K", "T_die_C", "mismatch_strain", "sigma_indicator_MPa"]


def main():
    data_path = ROOT / "data" / "package_dataset.csv"
    if not data_path.exists():
        raise SystemExit("Dataset not found. Run: python -m src.dataset_generation")
    df = pd.read_csv(data_path)
    X = df[FEATURES]
    X_train, X_test, idx_train, idx_test = train_test_split(
        X, df.index, test_size=0.20, random_state=42
    )
    models = {
        "LinearRegression": make_pipeline(StandardScaler(), LinearRegression()),
        "RandomForest": RandomForestRegressor(
            n_estimators=300, min_samples_leaf=2, random_state=42, n_jobs=-1
        ),
        "GradientBoosting": GradientBoostingRegressor(random_state=42),
    }
    results_dir = ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    metric_rows = []
    importance_rows = []
    for target in TARGETS:
        y = df[target]
        y_train, y_test = y.loc[idx_train], y.loc[idx_test]
        for name, model in models.items():
            model.fit(X_train, y_train)
            pred = model.predict(X_test)
            metric_rows.append({
                "target": target, "model": name,
                "R2": r2_score(y_test, pred),
                "MAE": mean_absolute_error(y_test, pred),
                "RMSE": mean_squared_error(y_test, pred) ** 0.5,
            })
            fitted = model[-1] if hasattr(model, "steps") else model
            if hasattr(fitted, "feature_importances_"):
                importance = fitted.feature_importances_
            elif hasattr(fitted, "coef_"):
                importance = abs(fitted.coef_)
            else:
                importance = None
            if importance is not None:
                for feature, value in zip(FEATURES, importance):
                    importance_rows.append({
                        "target": target, "model": name,
                        "feature": feature, "importance": float(value)
                    })
            fig, ax = plt.subplots(figsize=(5.5, 5))
            ax.scatter(y_test, pred, s=12, alpha=0.55)
            lo, hi = min(y_test.min(), pred.min()), max(y_test.max(), pred.max())
            ax.plot([lo, hi], [lo, hi], linestyle="--")
            ax.set_xlabel(f"Physics-model {target}")
            ax.set_ylabel(f"ML prediction {target}")
            ax.set_title(f"{target}: {name}")
            fig.tight_layout()
            fig.savefig(results_dir / f"parity_{target}_{name}.png", dpi=160)
            plt.close(fig)
    metrics = pd.DataFrame(metric_rows)
    metrics.to_csv(results_dir / "model_metrics.csv", index=False)
    importance_df = pd.DataFrame(importance_rows)
    importance_df.to_csv(results_dir / "feature_importance.csv", index=False)
    for target in TARGETS:
        subset = importance_df[
            (importance_df["target"] == target) &
            (importance_df["model"] == "GradientBoosting")
        ]
        if not subset.empty:
            subset = subset.sort_values("importance", ascending=True)
            fig, ax = plt.subplots(figsize=(7, 5))
            ax.barh(subset["feature"], subset["importance"])
            ax.set_xlabel("Model feature importance")
            ax.set_title(f"Gradient Boosting feature importance: {target}")
            fig.tight_layout()
            fig.savefig(results_dir / f"importance_{target}.png", dpi=160)
            plt.close(fig)
    print(metrics.to_string(index=False))
    print(f"\nMetrics and parity plots saved in {results_dir}")


if __name__ == "__main__":
    main()
