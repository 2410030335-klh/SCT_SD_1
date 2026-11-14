# SCT_SD_1 — Temperature Converter

A command-line Python program that converts values between Celsius, Fahrenheit, and Kelvin.

## Features
- Converts between all six scale directions.
- Accepts decimal and negative temperatures.
- Rejects invalid scale names and temperatures below absolute zero.
- Repeats conversions until the user enters `q`.

## Run
Requires Python 3.8 or newer. No third-party packages are needed.

```bash
python temperature_converter.py
```

## Conversion formulas
- °F = (°C × 9/5) + 32
- K = °C + 273.15
- °C = (°F − 32) × 5/9
- °C = K − 273.15

## Example checks
- 0 C → 32.00 F
- 100 C → 373.15 K
- 32 F → 0.00 C
