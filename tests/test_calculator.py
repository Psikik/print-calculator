"""Tests for core calculator functionality."""
import pytest
from print_calc.core.calculator import calculate_cost


def test_basic_calculation():
    """Test basic cost calculation."""
    result = calculate_cost(
        weight_g=100,
        time_hours=2,
        cost_per_kg=20,
        power_w=200,
        electricity_rate=0.12,
    )
    
    # Material: (100g / 1000) * $20 * 1.05 = $2.10
    assert round(result.material_cost, 2) == 2.10
    
    # Energy: (200W / 1000) * 2h * $0.12/kWh = $0.048
    assert round(result.energy_cost, 3) == 0.048
    
    # Total should be material + energy
    assert round(result.total, 2) == round(2.10 + 0.048, 2)


def test_with_machine_cost():
    """Test calculation with machine hourly rate."""
    result = calculate_cost(
        weight_g=50,
        time_hours=1,
        cost_per_kg=25,
        machine_hourly_rate=0.50,
    )
    
    # Machine cost: 1h * $0.50 = $0.50
    assert result.machine_cost == 0.50
    assert result.total > result.material_cost + result.energy_cost


def test_with_profit_margin():
    """Test calculation with profit margin."""
    result = calculate_cost(
        weight_g=100,
        time_hours=2,
        cost_per_kg=20,
        margin_percent=30,
    )
    
    # With 30% margin
    assert result.margin_percent == 30
    assert result.margin_amount == result.subtotal * 0.30
    assert result.total == result.subtotal + result.margin_amount


def test_zero_values():
    """Test calculation with zero optional values."""
    result = calculate_cost(
        weight_g=50,
        time_hours=1,
        cost_per_kg=20,
        machine_hourly_rate=0,
        margin_percent=0,
    )
    
    assert result.machine_cost == 0
    assert result.margin_amount == 0


def test_waste_factor():
    """Test waste factor calculation."""
    # With default 5% waste
    result1 = calculate_cost(
        weight_g=100,
        time_hours=1,
        cost_per_kg=20,
    )
    
    # With 10% waste
    result2 = calculate_cost(
        weight_g=100,
        time_hours=1,
        cost_per_kg=20,
        waste_factor=10,
    )
    
    assert result2.material_cost > result1.material_cost


def test_additional_costs():
    """Test additional costs."""
    result = calculate_cost(
        weight_g=50,
        time_hours=1,
        cost_per_kg=20,
        additional_costs=5.00,
    )
    
    assert result.additional_costs == 5.00
    assert result.subtotal == result.material_cost + result.energy_cost + result.machine_cost + 5.00
