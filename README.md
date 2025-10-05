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
- **uv** - Fast Python package manager
- **Typer** - Modern CLI framework
- **Rich** - Beautiful terminal output
- **Pydantic** - Data validation

## Quick Start

```bash
# Initialize project with uv
uv init print-calculator
cd print-calculator

# Add dependencies
uv add typer rich pydantic questionary pyyaml
uv add --dev pytest pytest-cov black ruff mypy

# Run the calculator (after implementation)
uv run print-calc gcode model.gcode

# Or use manual input
uv run print-calc manual --weight 45 --time 3.5 --material-cost 20
```

## Installation

```bash
# Install from PyPI with uv (when published)
uv pip install print-calc

# Or use traditional pip
pip install print-calc

# Or use pipx for isolated installation
pipx install print-calc

# Run without installation using uvx
uvx print-calc gcode model.gcode
```

## Development

```bash
# Install in development mode
uv pip install -e .

# Run tests
uv run pytest

# Format code
uv run black src/

# Lint code
uv run ruff check src/
```

## Documentation

See [PLAN.md](PLAN.md) for detailed project planning and architecture.

## Development Status

🚧 **In Development** - This project is currently being built. Check the roadmap in PLAN.md for progress.
