# Date Calculator

A simple graphical program built with Python and Tkinter to calculate a future date based on an initial date and a number of days. The program also identifies the next business day after the calculated date, displaying the results in both English and Portuguese (Brazil).

## Features

- Automatically formats the input date as `DD/MM/YYYY`.
- Calculates the final date based on an initial date and a specified number of days.
- Identifies and displays the day of the week for the calculated date in Portuguese.
- Finds the next business day if the calculated date falls on a weekend and displays the corresponding day in Portuguese.

## Requirements

- Python 3.x
- Tkinter library (included with most Python installations)

## How to Use

1. Enter the starting date in the format `DD/MM/YYYY` in the "Initial Date" field.
   - The field will automatically format as you type.
2. Enter the number of days in the "Number of Days" field.
3. Click the "Calculate Final Date" button.
4. The program will display:
   - The calculated final date with the day of the week in Portuguese.
   - The next business day if the final date falls on a weekend, along with the day of the week in Portuguese.

## Installation and Execution

1. Make sure Python 3.x is installed on your computer.
2. Clone or download this repository.
3. Run the program using the command:

   ```bash
   python date_calculator.py
   ```
