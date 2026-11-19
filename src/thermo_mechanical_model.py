"""First-order CTE mismatch strain and constrained stress indicator."""
from __future__ import annotations


def mismatch_strain(alpha_die_1_K, alpha_substrate_1_K, deltaT_K):
    """Return absolute relative thermal mismatch strain [-]."""
    if deltaT_K < 0:
        raise ValueError("deltaT_K must be non-negative in this model.")
    return abs(alpha_die_1_K - alpha_substrate_1_K) * deltaT_K


def constrained_stress_indicator(strain, E_eff_Pa, nu_eff):
    """Return idealized fully constrained biaxial stress indicator [Pa]."""
    if strain < 0:
        raise ValueError("Strain magnitude must be non-negative.")
    if E_eff_Pa <= 0:
        raise ValueError("Effective modulus must be positive.")
    if not (0.0 <= nu_eff < 0.5):
        raise ValueError("nu_eff must be in [0, 0.5) for this isotropic approximation.")
    return E_eff_Pa / (1.0 - nu_eff) * strain
