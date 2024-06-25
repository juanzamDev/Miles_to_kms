# Kilometer to Miles Converter

A simple Tkinter-based GUI application to convert kilometers to miles.

## Features

- Input the distance in kilometers
- Click the "Calculate" button to see the equivalent distance in miles
- User-friendly interface with Tkinter

## Requirements

- Python 3.x
- Tkinter (usually included with Python standard library)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    ```
2. **Navigate to the project directory**:
    ```sh
    cd your-repo-name
    ```

## Usage

1. **Run the application**:
    ```sh
    python your_script_name.py
    ```
2. **Input the distance in kilometers**.
3. **Click the "Calculate" button** to see the distance in miles.

## Code Overview

Here's a brief overview of the main components of the application:

- **Main Window**: Sets up the Tkinter main window with size and padding configurations.
- **Converter Function**: A function to convert kilometers to miles and update the result label.
- **Widgets**: Entry widget for input, labels for displaying text, and a button to trigger the conversion.

## Example Code

```python
from tkinter import *

# Create the main window
root = Tk()
root.minsize(width=100, height=150)
root.config(padx=30, pady=30)

# Function to convert kilometers to miles
def converter():
    try:
        number = float(input.get())
        miles = number * 0.621371
        result_label.config(text=f"Is equal to {miles:.2f} miles")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create an entry for kilometers
input = Entry(root, width=10)
input.grid(row=0, column=1)

# Create label "Km"
input_label = Label(root, text="Km", font=("Arial", 12))
input_label.grid(row=0, column=2)

# Create result label in the second line
result_label = Label(root, text="Is equal to 0 miles", font=("Arial", 12))
result_label.grid(row=1, column=1, columnspan=2)

# Create and pack a button
button = Button(root, text="Calculate", command=converter)
button.grid(row=2, column=1)

# Start the Tkinter event loop
root.mainloop()
