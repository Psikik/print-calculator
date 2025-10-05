# Print Calculator CLI

A Python command-line tool for calculating the cost of 3D prints with support for G-code analysis, material management, and detailed cost breakdowns.

## Features

- 📊 Calculate costs from G-code files or manual input
- 🎨 Manage material presets and printer profiles
- 💰 Detailed cost breakdown (material, energy, machine time)
- 📈 Profit margin calculations
- 📄 Multiple output formats (table, JSON, CSV, Markdown)
- 🔧 Interactive mode for easy input
- ✨ Beautiful terminal output with Rich

## Tech Stack

- **Python 3.8+**
- **Typer** - Modern CLI framework
- **Rich** - Beautiful terminal output
- **Pydantic** - Data validation

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Or with Poetry
poetry install

# Run the calculator
python -m print_calc gcode model.gcode

# Or use manual input
python -m print_calc manual --weight 45 --time 3.5 --material-cost 20
```

## Installation

```bash
# Install from PyPI (when published)
pip install print-calc

# Or use pipx for isolated installation
pipx install print-calc
```

## Documentation

See [PLAN.md](PLAN.md) for detailed project planning and architecture.

## Development Status

🚧 **In Development** - This project is currently being built. Check the roadmap in PLAN.md for progress.
