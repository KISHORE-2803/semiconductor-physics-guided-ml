import pytest

from src.thermal_model import thermal_resistance, thermal_response
from src.thermo_mechanical_model import mismatch_strain, constrained_stress_indicator


def test_thermal_resistance_hand_calculation():
    # 1 mm / (2 W/mK * 1 m2) = 5e-4 K/W
    assert thermal_resistance([1e-3], [2.0], 1.0) == pytest.approx(5e-4)


def test_power_increases_temperature_rise():
    a = thermal_response([1e-3], [1.0], 1.0, 1.0, 25.0)
    b = thermal_response([1e-3], [1.0], 1.0, 2.0, 25.0)
    assert b["deltaT_K"] > a["deltaT_K"]


def test_conductivity_increase_reduces_resistance():
    low_k = thermal_resistance([1e-3], [1.0], 1.0)
    high_k = thermal_resistance([1e-3], [2.0], 1.0)
    assert high_k < low_k


def test_cte_mismatch_strain():
    eps = mismatch_strain(3e-6, 15e-6, 100.0)
    assert eps == pytest.approx(0.0012)


def test_stress_indicator_positive():
    stress = constrained_stress_indicator(1e-3, 10e9, 0.3)
    assert stress > 0
