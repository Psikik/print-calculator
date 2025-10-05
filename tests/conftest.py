"""Test configuration and fixtures."""
import pytest


@pytest.fixture
def sample_print_params():
    """Sample parameters for a typical 3D print."""
    return {
        "weight_g": 45.0,
        "time_hours": 3.5,
        "cost_per_kg": 20.0,
        "power_w": 200.0,
        "electricity_rate": 0.12,
    }
