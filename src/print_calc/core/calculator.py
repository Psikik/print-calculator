"""Core calculation logic for 3D print costs."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class CostBreakdown:
    """Detailed cost breakdown for a 3D print."""
    material_cost: float
    energy_cost: float
    machine_cost: float
    additional_costs: float
    subtotal: float
    margin_amount: float
    total: float
    
    # Input parameters for reference
    weight_g: float
    time_hours: float
    cost_per_kg: float
    power_w: float
    electricity_rate: float
    machine_hourly_rate: float
    margin_percent: float


def calculate_cost(
    weight_g: float,
    time_hours: float,
    cost_per_kg: float,
    power_w: float = 200.0,
    electricity_rate: float = 0.12,
    machine_hourly_rate: float = 0.0,
    additional_costs: float = 0.0,
    margin_percent: float = 0.0,
    waste_factor: float = 5.0,
) -> CostBreakdown:
    """
    Calculate total cost of 3D print.
    
    Args:
        weight_g: Filament weight in grams
        time_hours: Print time in hours
        cost_per_kg: Material cost per kilogram
        power_w: Power consumption in watts
        electricity_rate: Electricity rate per kWh
        machine_hourly_rate: Machine hourly operating rate
        additional_costs: Any additional costs
        margin_percent: Profit margin percentage
        waste_factor: Material waste percentage (default 5%)
        
    Returns:
        CostBreakdown with detailed cost information
    """
    # Material Cost (including waste factor)
    material_cost = (weight_g / 1000) * cost_per_kg * (1 + waste_factor / 100)
    
    # Energy Cost
    energy_cost = (power_w / 1000) * time_hours * electricity_rate
    
    # Machine Cost
    machine_cost = time_hours * machine_hourly_rate
    
    # Subtotal
    subtotal = material_cost + energy_cost + machine_cost + additional_costs
    
    # With Profit Margin
    margin_amount = subtotal * (margin_percent / 100)
    total = subtotal + margin_amount
    
    return CostBreakdown(
        material_cost=material_cost,
        energy_cost=energy_cost,
        machine_cost=machine_cost,
        additional_costs=additional_costs,
        subtotal=subtotal,
        margin_amount=margin_amount,
        total=total,
        weight_g=weight_g,
        time_hours=time_hours,
        cost_per_kg=cost_per_kg,
        power_w=power_w,
        electricity_rate=electricity_rate,
        machine_hourly_rate=machine_hourly_rate,
        margin_percent=margin_percent,
    )
