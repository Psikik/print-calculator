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
- **Language**: Node.js (JavaScript/TypeScript) or Python
- **CLI Framework**: 
  - Node.js: Commander.js or Yargs + Inquirer (for interactive)
  - Python: Click or Typer + Rich (for beautiful output)
- **G-code Parser**: Custom parser or existing library
- **Output Formatting**: 
  - Tables: cli-table3 (Node) or rich.table (Python)
  - Colors: chalk (Node) or rich (Python)
- **Config Storage**: JSON/YAML files in user home directory
- **Testing**: Jest (Node) or pytest (Python)

### Project Structure
```
print-calculator/
├── src/
│   ├── commands/
│   │   ├── gcode.js          # G-code calculation command
│   │   ├── manual.js          # Manual input command
│   │   ├── interactive.js     # Interactive mode
│   │   ├── material.js        # Material management
│   │   ├── printer.js         # Printer management
│   │   └── config.js          # Configuration management
│   ├── lib/
│   │   ├── calculator.js      # Core calculation logic
│   │   ├── gcode-parser.js    # G-code parsing
│   │   ├── config-manager.js  # Config file handling
│   │   └── formatters.js      # Output formatters
│   ├── utils/
│   │   ├── validation.js      # Input validation
│   │   └── helpers.js         # Utility functions
│   └── index.js               # CLI entry point
├── config/
│   ├── materials.json         # Default materials
│   └── defaults.json          # Default settings
├── tests/
│   ├── calculator.test.js
│   ├── gcode-parser.test.js
│   └── commands.test.js
├── package.json
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

### Core Formulas

```javascript
// Material Cost
const materialCost = (weight_g / 1000) * cost_per_kg * (1 + waste_factor / 100);

// Energy Cost
const energyCost = (power_w / 1000) * time_hours * electricity_rate;

// Machine Cost
const machineCost = time_hours * machine_hourly_rate;

// Total Cost
const subtotal = materialCost + energyCost + machineCost + additionalCosts;

// With Profit Margin
const total = subtotal * (1 + margin_percent / 100);
```

### G-code Parsing Logic

```javascript
function parseGcode(fileContent) {
  const metadata = {
    filamentUsed: 0,
    printTime: 0,
    material: null
  };

  // Extract from slicer comments
  // Cura: ;Filament used: 1.23m
  // PrusaSlicer: ; filament used [g] = 45.2
  // Extract time estimates
  // ;TIME:12345 (seconds)
  
  return metadata;
}
```

## Development Roadmap

### Phase 1: MVP (Weeks 1-2)
- [ ] Project setup (Node.js/TypeScript or Python)
- [ ] Basic CLI structure with Commander/Click
- [ ] Manual calculation command
- [ ] Simple terminal output
- [ ] Basic calculation logic
- [ ] Unit tests for calculations

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

### NPM Package (Node.js)
```bash
# Install globally
npm install -g print-calc

# Or use with npx
npx print-calc gcode model.gcode
```

### Python Package (PyPI)
```bash
# Install globally
pip install print-calc

# Or use with pipx
pipx run print-calc gcode model.gcode
```

### Binary Distribution
- Package as standalone binary using pkg (Node) or PyInstaller (Python)
- Support Windows, macOS, Linux
- No runtime dependencies

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
# 1. Initialize the project
npm init -y
npm install commander inquirer chalk cli-table3

# 2. Create basic structure
mkdir -p src/{commands,lib,utils}
touch src/index.js src/lib/calculator.js

# 3. Set up CLI entry point
# Add to package.json:
# "bin": { "print-calc": "./src/index.js" }

# 4. Start development
npm link  # Test locally
```

### First Milestone
Build a working manual calculator that:
1. Takes input via CLI flags
2. Calculates material + energy + machine costs
3. Displays formatted output
4. Has basic error handling

This serves as the foundation for all other features.
