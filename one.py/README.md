# Unit Conversion System

**PS No.:** 17  
**Course:** Bachelor of Technology – Computer Science and Engineering  
**Language:** Python 3

## Problem statement
Create a menu-driven converter that converts values between units of length, weight, temperature and time.

## Conversions
1. Kilometers to miles: `miles = kilometers * 0.621371`
2. Kilograms to grams: `grams = kilograms * 1000`
3. Celsius to Fahrenheit: `fahrenheit = (celsius * 9 / 5) + 32`
4. Hours to minutes: `minutes = hours * 60`

All results are displayed to 2 decimal places.

## How to run
1. Install Python 3.
2. Open a terminal in this folder.
3. Run: `python unit_conversion_system.py`

## Validation
- Only menu choices 1 to 5 are accepted.
- Non-numeric values are rejected with `Invalid value. Enter a number.`
- Negative distance, weight and time are rejected.
- Negative Celsius values are allowed because temperatures can be below zero.
- Option 5 exits the program.

## Test cases
| Test | Input | Expected output |
|---|---|---|
| Normal | Choice 1, 5 km | 5 km = 3.11 miles |
| Boundary | Choice 3, 0 C | 0 C = 32.00 F |
| Invalid menu | Choice 7 | Invalid choice. Select 1 to 5. |
| Invalid value | Choice 1, `abc` | Invalid value. Enter a number. |
| Weight | Choice 2, 2 kg | 2 kg = 2000.00 g |
| Temperature | Choice 3, 100 C | 100 C = 212.00 F |
| Time | Choice 4, 2 hours | 2 hours = 120.00 minutes |

## GitHub submission
Create a new public or private GitHub repository named `unit-conversion-system`, then upload:
- `unit_conversion_system.py`
- `README.md`
- `Unit_Conversion_System_Report.docx`

Suggested repository description: `A menu-driven Python 3 program for converting length, weight, temperature and time units.`
