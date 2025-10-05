"""Main CLI entry point for print-calc."""
import typer
from rich.console import Console

app = typer.Typer(
    name="print-calc",
    help="3D Print Cost Calculator CLI",
    add_completion=False,
)
console = Console()


@app.command()
def manual(
    weight: float = typer.Option(..., "--weight", "-w", help="Filament weight in grams"),
    time: float = typer.Option(..., "--time", "-t", help="Print time in hours"),
    material_cost: float = typer.Option(20.0, "--material-cost", help="Cost per kg"),
    power: float = typer.Option(200.0, "--power", help="Power consumption in watts"),
    rate: float = typer.Option(0.12, "--rate", help="Electricity rate per kWh"),
    machine_rate: float = typer.Option(0.0, "--machine-rate", help="Machine hourly rate"),
    margin: float = typer.Option(0.0, "--margin", help="Profit margin percentage"),
):
    """Calculate cost from manual input."""
    from rich.table import Table
    
    # Calculate costs
    material_cost_total = (weight / 1000) * material_cost
    energy_cost = (power / 1000) * time * rate
    machine_cost = time * machine_rate
    subtotal = material_cost_total + energy_cost + machine_cost
    margin_amount = subtotal * (margin / 100)
    total = subtotal + margin_amount
    
    # Display results
    table = Table(title="💰 Cost Breakdown", show_header=False)
    table.add_column("Item", style="cyan", width=20)
    table.add_column("Cost", style="green", justify="right")
    
    table.add_row("Filament Weight", f"{weight}g")
    table.add_row("Print Time", f"{time}h")
    table.add_row("")
    table.add_row("Material Cost", f"${material_cost_total:.2f}")
    table.add_row("Energy Cost", f"${energy_cost:.2f}")
    if machine_cost > 0:
        table.add_row("Machine Cost", f"${machine_cost:.2f}")
    table.add_row("─" * 20, "─" * 10)
    table.add_row("Subtotal", f"${subtotal:.2f}")
    if margin > 0:
        table.add_row(f"Margin ({margin}%)", f"${margin_amount:.2f}")
        table.add_row("─" * 20, "─" * 10)
        table.add_row("[bold]Total Price[/bold]", f"[bold]${total:.2f}[/bold]")
    else:
        table.add_row("[bold]Total Cost[/bold]", f"[bold]${total:.2f}[/bold]")
    
    console.print()
    console.print(table)
    console.print()


@app.command()
def version():
    """Show version information."""
    console.print("[cyan]print-calc[/cyan] version [green]0.1.0[/green]")


if __name__ == "__main__":
    app()
