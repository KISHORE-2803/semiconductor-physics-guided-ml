"""Reduced-order steady 1-D thermal resistance model."""
from __future__ import annotations

def thermal_resistance(thickness_m, conductivity_W_mK, area_m2):
    """Return equivalent series thermal resistance [K/W]."""
    if len(thickness_m) != len(conductivity_W_mK):
        raise ValueError("Thickness and conductivity arrays must have equal length.")
    if area_m2 <= 0:
        raise ValueError("Area must be positive.")
    if any(t <= 0 for t in thickness_m):
        raise ValueError("All layer thicknesses must be positive.")
    if any(k <= 0 for k in conductivity_W_mK):
        raise ValueError("All thermal conductivities must be positive.")
    return sum(t / (k * area_m2) for t, k in zip(thickness_m, conductivity_W_mK))

def thermal_response(thickness_m, conductivity_W_mK, area_m2, power_W, ambient_C):
    """Return Rth [K/W], deltaT [K], and estimated die temperature [°C]."""
    if power_W < 0:
        raise ValueError("Power must be non-negative for this model.")
    rth = thermal_resistance(thickness_m, conductivity_W_mK, area_m2)
    delta_t = power_W * rth
    return {"R_th_K_W": rth, "deltaT_K": delta_t, "T_die_C": ambient_C + delta_t}
