# 3D Print Cost Calculator CLI - Project Plan

## Overview
A command-line interface (CLI) tool for calculating the cost of 3D prints, supporting manual input, G-code file analysis, and configuration management.

## Core Features

### 1. Basic Cost Calculation
- Calculate costs based on:
  - Filament weight (grams)
  - Print time (hours/minutes)
  - Material type and cost per kg
  - Electricity consumption and rate
  - Machine depreciation/hourly rate
  - Optional markup/profit margin

### 2. G-code Analysis
- Parse G-code files to extract:
  - Filament usage (length and weight)
  - Estimated print time
  - Material type (from slicer metadata)
  - Layer height, infill, etc.
- Support popular slicer formats:
  - Cura
  - PrusaSlicer
  - Simplify3D
  - Others with standard G-code comments

### 3. Configuration Management
- Material presets (save commonly used materials)
- Printer profiles (power consumption, hourly rate)
- Default settings (electricity rate, currency)
- Export/import configurations

### 4. Output Formats
- Terminal output (formatted table)
- JSON (for integration with other tools)
- CSV (for spreadsheet import)
- Markdown (for documentation)
- PDF invoice/quote (optional)

## CLI Commands Structure

### Main Commands

```bash
# Calculate from G-code file
print-calc gcode <file.gcode> [options]

# Calculate from manual input
print-calc manual [options]

# Interactive mode
print-calc interactive

# Manage materials
print-calc material <add|list|edit|remove> [name]

# Manage printer profiles
print-calc printer <add|list|edit|remove> [name]

# Configuration
print-calc config <get|set|list> [key] [value]

# Export/Import settings
print-calc export <file>
print-calc import <file>

# Display help
print-calc help [command]
print-calc --version
```

### Command Examples

```bash
# Quick calculation from G-code
print-calc gcode model.gcode --material PLA --printer "Prusa i3"

# Manual calculation with all parameters
print-calc manual \
  --weight 25 \
  --time 3.5 \
  --material-cost 20 \
  --power 200 \
  --rate 0.12 \
  --margin 30

# Interactive mode (prompts for each input)
print-calc interactive

# Add a new material
print-calc material add "PLA+" --cost 25 --density 1.24

# List all materials
print-calc material list

# Set default electricity rate
print-calc config set electricity-rate 0.12

# Export detailed breakdown as JSON
print-calc gcode model.gcode --output json --file report.json

# Generate invoice
print-calc gcode model.gcode --invoice --client "John Doe" --output pdf
```

## Options and Flags

### Global Options
```
-v, --verbose          Show detailed information
-q, --quiet           Minimal output
-o, --output <format> Output format (table|json|csv|md)
-f, --file <path>     Save output to file
--no-color            Disable colored output
--currency <code>     Currency code (USD, EUR, GBP, etc.)
```

### G-code Command Options
```
--material <name>     Override material from G-code
--printer <name>      Use printer profile
--margin <percent>    Add profit margin
--additional <cost>   Additional costs
--waste <percent>     Material waste factor (default: 5%)
```

### Manual Command Options
```
-w, --weight <grams>       Filament weight
-t, --time <hours>         Print time
--material-cost <price>    Cost per kg
--power <watts>            Power consumption
--rate <price>             Electricity rate per kWh
--machine-rate <price>     Machine hourly rate
--margin <percent>         Profit margin
--additional <cost>        Additional costs
```

## Output Examples

### Terminal Table Output
```
╔══════════════════════════════════════════╗
║     3D PRINT COST CALCULATION           ║
╠══════════════════════════════════════════╣
║ File: dragon_model.gcode                 ║
║ Material: PLA                            ║
║ Printer: Prusa i3 MK3S                  ║
╠══════════════════════════════════════════╣
║ COST BREAKDOWN                           ║
╟──────────────────────────────────────────╢
║ Filament Used:        45.2g              ║
║ Material Cost:        $0.90              ║
║                                          ║
║ Print Time:           3h 24m             ║
║ Energy Cost:          $0.08              ║
║ Machine Time:         $1.70              ║
║                                          ║
║ Additional Costs:     $0.50              ║
║ Subtotal:             $3.18              ║
║                                          ║
║ Profit Margin (30%):  $0.95              ║
╟──────────────────────────────────────────╢
║ TOTAL COST:           $4.13              ║
║ SELLING PRICE:        $4.13              ║
╚══════════════════════════════════════════╝
```

### JSON Output
```json
{
  "file": "dragon_model.gcode",
  "material": "PLA",
  "printer": "Prusa i3 MK3S",
  "breakdown": {
    "material": {
      "weight_g": 45.2,
      "cost_per_kg": 20,
      "cost": 0.90
    },
    "energy": {
      "print_time_hours": 3.4,
      "power_w": 200,
      "rate_per_kwh": 0.12,
      "cost": 0.08
    },
    "machine": {
      "time_hours": 3.4,
      "hourly_rate": 0.50,
      "cost": 1.70
    },
    "additional": 0.50,
    "subtotal": 3.18,
    "margin_percent": 30,
    "margin_amount": 0.95
  },
  "total": 4.13,
  "currency": "USD"
}
```

## Technical Architecture

### Technology Stack
- **Language**: Python 3.8+
- **CLI Framework**: Typer (modern, type-hint based CLI) or Click
- **Output Formatting**: Rich (beautiful terminal output with colors, tables, progress bars)
- **Interactive Prompts**: questionary or rich.prompt
- **G-code Parser**: Custom parser using regular expressions
- **Config Storage**: JSON/YAML files in user home directory (`~/.print-calc/`)
- **Data Validation**: Pydantic (for type safety and validation)
- **PDF Generation**: ReportLab or weasyprint (optional)
- **Testing**: pytest + pytest-cov for coverage
- **Package Management**: Poetry or pip with requirements.txt

### Project Structure
```
print-calculator/
├── print_calc/
│   ├── __init__.py
│   ├── cli.py                 # Main CLI entry point (Typer app)
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── gcode.py           # G-code calculation command
│   │   ├── manual.py          # Manual input command
│   │   ├── interactive.py     # Interactive mode
│   │   ├── material.py        # Material management
│   │   ├── printer.py         # Printer management
│   │   └── config.py          # Configuration management
│   ├── core/
│   │   ├── __init__.py
│   │   ├── calculator.py      # Core calculation logic
│   │   ├── gcode_parser.py    # G-code parsing
│   │   ├── config_manager.py  # Config file handling
│   │   └── models.py          # Pydantic models for data
│   ├── output/
│   │   ├── __init__.py
│   │   ├── formatters.py      # Output formatters
│   │   └── templates.py       # Invoice/report templates
│   └── utils/
│       ├── __init__.py
│       ├── validation.py      # Input validation
│       └── helpers.py         # Utility functions
├── config/
│   ├── materials.json         # Default materials
│   └── defaults.json          # Default settings
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_gcode_parser.py
│   ├── test_commands.py
│   └── conftest.py            # pytest fixtures
├── pyproject.toml             # Poetry config (or setup.py)
├── requirements.txt           # Dependencies
├── README.md
└── PLAN.md
```

### Configuration Files

#### ~/.print-calc/config.json
```json
{
  "electricity_rate": 0.12,
  "currency": "USD",
  "default_material": "PLA",
  "default_printer": "generic",
  "waste_factor": 5,
  "output_format": "table"
}
```

#### ~/.print-calc/materials.json
```json
{
  "PLA": {
    "cost_per_kg": 20,
    "density": 1.24,
    "type": "thermoplastic"
  },
  "PETG": {
    "cost_per_kg": 25,
    "density": 1.27,
    "type": "thermoplastic"
  }
}
```

#### ~/.print-calc/printers.json
```json
{
  "Prusa i3 MK3S": {
    "power_consumption": 200,
    "hourly_rate": 0.50,
    "build_volume": "250x210x210"
  }
}
```

## Calculation Logic

### Calculation Logic

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class CostBreakdown:
    material_cost: float
    energy_cost: float
    machine_cost: float
    additional_costs: float
    subtotal: float
    margin_amount: float
    total: float

def calculate_cost(
    weight_g: float,
    time_hours: float,
    cost_per_kg: float,
    power_w: float,
    electricity_rate: float,
    machine_hourly_rate: float = 0.0,
    additional_costs: float = 0.0,
    margin_percent: float = 0.0,
    waste_factor: float = 5.0
) -> CostBreakdown:
    """Calculate total cost of 3D print."""
    
    # Material Cost
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
        total=total
    )
```

### G-code Parsing Logic

```python
import re
from typing import Optional, Dict
from pathlib import Path

class GCodeParser:
    """Parse G-code files to extract print metadata."""
    
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.content = filepath.read_text()
    
    def parse(self) -> Dict[str, any]:
        """Extract metadata from G-code file."""
        metadata = {
            'filament_weight_g': 0.0,
            'filament_length_m': 0.0,
            'print_time_hours': 0.0,
            'material_type': None,
            'slicer': None
        }
        
        # Detect slicer
        if 'Cura' in self.content:
            metadata['slicer'] = 'Cura'
            metadata.update(self._parse_cura())
        elif 'PrusaSlicer' in self.content or 'Slic3r' in self.content:
            metadata['slicer'] = 'PrusaSlicer'
            metadata.update(self._parse_prusaslicer())
        else:
            metadata.update(self._parse_generic())
        
        return metadata
    
    def _parse_cura(self) -> Dict:
        """Parse Cura-specific metadata."""
        data = {}
        
        # ;Filament used: 1.23456m
        filament_match = re.search(r';Filament used: ([\d.]+)m', self.content)
        if filament_match:
            data['filament_length_m'] = float(filament_match.group(1))
        
        # ;TIME:12345
        time_match = re.search(r';TIME:([\d]+)', self.content)
        if time_match:
            data['print_time_hours'] = int(time_match.group(1)) / 3600
        
        return data
    
    def _parse_prusaslicer(self) -> Dict:
        """Parse PrusaSlicer-specific metadata."""
        data = {}
        
        # ; filament used [g] = 45.2
        weight_match = re.search(r'; filament used \[g\] = ([\d.]+)', self.content)
        if weight_match:
            data['filament_weight_g'] = float(weight_match.group(1))
        
        # ; estimated printing time (normal mode) = 3h 24m 15s
        time_match = re.search(r'; estimated printing time.*= (\d+)h (\d+)m', self.content)
        if time_match:
            hours = int(time_match.group(1))
            minutes = int(time_match.group(2))
            data['print_time_hours'] = hours + minutes / 60
        
        return data
    
    def _parse_generic(self) -> Dict:
        """Fallback generic parser."""
        # Try to find any time/filament mentions
        return {}
```

## Development Roadmap

### Phase 1: MVP (Weeks 1-2)
- [ ] Project setup with Poetry/pip (Python 3.8+)
- [ ] Basic CLI structure with Typer
- [ ] Manual calculation command
- [ ] Rich terminal output with tables
- [ ] Basic calculation logic with Pydantic models
- [ ] Unit tests with pytest

### Phase 2: G-code Support (Week 3)
- [ ] G-code parser implementation
- [ ] Support for Cura/PrusaSlicer formats
- [ ] Filament and time extraction
- [ ] G-code command implementation
- [ ] Tests for parser

### Phase 3: Configuration (Week 4)
- [ ] Config file management
- [ ] Material presets (add/list/edit/remove)
- [ ] Printer profiles
- [ ] Default settings management
- [ ] Export/import functionality

### Phase 4: Enhanced UX (Week 5)
- [ ] Interactive mode with prompts
- [ ] Colored terminal output
- [ ] Beautiful table formatting
- [ ] Progress indicators for file processing
- [ ] Error handling and validation

### Phase 5: Output Formats (Week 6)
- [ ] JSON output
- [ ] CSV export
- [ ] Markdown reports
- [ ] Optional PDF generation
- [ ] File output support

### Phase 6: Polish & Release (Week 7-8)
- [ ] Comprehensive documentation
- [ ] More unit tests (>80% coverage)
- [ ] Integration tests
- [ ] Package for npm/pip
- [ ] CI/CD setup
- [ ] Version 1.0 release

## Installation & Distribution

### PyPI Package
```bash
# Install globally
pip install print-calc

# Or use with pipx (recommended for CLI tools)
pipx install print-calc

# Run directly with pipx
pipx run print-calc gcode model.gcode

# Development installation
pip install -e .
```

### Poetry Installation (Development)
```bash
# Install dependencies
poetry install

# Run the CLI
poetry run print-calc gcode model.gcode

# Build package
poetry build
```

### Binary Distribution
- Package as standalone binary using PyInstaller or Nuitka
- Support Windows, macOS, Linux
- No Python runtime dependencies for end users

## Success Metrics
- Parse 95%+ of G-code files correctly
- Calculate costs in <1 second for G-code files
- Support 10+ material types out of box
- Intuitive command structure (<5 min learning curve)
- Comprehensive help documentation
- Cross-platform compatibility

## Future Enhancements
- Multi-file batch processing
- Cost comparison between materials
- Historical cost tracking and trends
- Cloud sync for configurations
- Web dashboard companion
- Slicer plugins for direct integration
- Support for resin printers
- API server mode for integrations
- Auto-update material prices from online sources
- Multi-language support
- Template system for invoices/quotes

## Getting Started

### Quick Start Commands
```bash
# 1. Initialize Python project with Poetry
poetry init --name print-calc --dependency typer --dependency rich

# Or with pip
mkdir print_calc
touch print_calc/__init__.py print_calc/cli.py

# 2. Install dependencies
poetry add typer rich pydantic
poetry add --group dev pytest pytest-cov black ruff

# Or with pip
pip install typer rich pydantic pytest black ruff

# 3. Create basic CLI structure
touch print_calc/cli.py

# 4. Set up entry point in pyproject.toml
# [tool.poetry.scripts]
# print-calc = "print_calc.cli:app"

# 5. Start development
poetry install
poetry run print-calc --help
```

### Essential Python Dependencies
```toml
[tool.poetry.dependencies]
python = "^3.8"
typer = "^0.9.0"           # CLI framework
rich = "^13.0.0"           # Beautiful terminal output
pydantic = "^2.0.0"        # Data validation
questionary = "^2.0.0"     # Interactive prompts
pyyaml = "^6.0.0"          # YAML config support

[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
pytest-cov = "^4.0.0"
black = "^23.0.0"          # Code formatter
ruff = "^0.1.0"            # Linter
mypy = "^1.0.0"            # Type checker
```

### First Milestone
Build a working manual calculator that:
1. Takes input via CLI flags using Typer
2. Calculates material + energy + machine costs
3. Displays formatted output with Rich tables
4. Has basic error handling and validation with Pydantic
5. Includes unit tests with pytest

This serves as the foundation for all other features.

### Example CLI Entry Point (cli.py)
```python
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="3D Print Cost Calculator CLI")
console = Console()

@app.command()
def manual(
    weight: float = typer.Option(..., "--weight", "-w", help="Filament weight in grams"),
    time: float = typer.Option(..., "--time", "-t", help="Print time in hours"),
    material_cost: float = typer.Option(20.0, "--material-cost", help="Cost per kg"),
    power: float = typer.Option(200.0, "--power", help="Power consumption in watts"),
    rate: float = typer.Option(0.12, "--rate", help="Electricity rate per kWh"),
    margin: float = typer.Option(0.0, "--margin", help="Profit margin percentage"),
):
    """Calculate cost from manual input."""
    
    # Calculate costs
    material_cost_total = (weight / 1000) * material_cost
    energy_cost = (power / 1000) * time * rate
    total = material_cost_total + energy_cost
    total_with_margin = total * (1 + margin / 100)
    
    # Display results
    table = Table(title="Cost Breakdown")
    table.add_column("Item", style="cyan")
    table.add_column("Cost", style="green")
    
    table.add_row("Material", f"${material_cost_total:.2f}")
    table.add_row("Energy", f"${energy_cost:.2f}")
    table.add_row("Total", f"${total_with_margin:.2f}")
    
    console.print(table)

if __name__ == "__main__":
    app()
```
