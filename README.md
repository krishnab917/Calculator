# Calculator

A clean and intuitive calculator application built with Python and Tkinter. Perform arithmetic operations with a simple graphical interface that displays the complete equation alongside the result.

##  Features

- **Full Arithmetic Support**: Addition, subtraction, multiplication, and division
   **Elegant GUI**: 4x4 button grid with number pad and operation buttons
-  **Complete Equation Display**: Shows the calculation equation with result (e.g., "5 + 3 = 8")
- **Robust Error Handling**: Catches invalid expressions and division by zero
-  **Always-on-Top Window**: Calculator stays visible on your desktop
-  **Decimal Support**: Perform calculations with decimal numbers

## 📋 Requirements

- Python 3.x
- Tkinter (included with most Python installations)

##  Quick Start

```bash
python calculator.py
```

The calculator window will open with a clean interface. Simply click the buttons to enter your calculation and press `=` to see the result.

##  Usage Examples

1. Calculate **5 + 3**: Click 5 → + → 3 → = (displays "5+3 = 8")
2. Calculate **10 * 2.5**: Click 1 → 0 → * → 2 → . → 5 → = (displays "10*2.5 = 25.0")
3. Divide **20 / 4**: Click 2 → 0 → / → 4 → = (displays "20/4 = 5.0")

##  Architecture

The application consists of two main classes:

### Calculator Class
- Handles core arithmetic operations
- Includes methods for `add()`, `subtract()`, `multiply()`, and `divide()`
- Validates division by zero

### CalculatorGUI Class
- Manages the Tkinter graphical interface
- Creates and positions buttons in a grid layout
- Processes button clicks and updates the display
- Evaluates expressions when the equals button is pressed

##  Error Handling

- **Invalid Expressions**: Shows an error dialog if you enter an invalid calculation
- **Division by Zero**: Prevented in the divide method

##  License

MIT
