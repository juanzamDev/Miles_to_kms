from tkinter import *

# Create the main window
root = Tk()
root.minsize(width=100, height=150)
root.config(padx=30, pady=30)

# Calculate  miles to km
def converter():
  number = float(input.get())
  kms = number * 1.621371
  result_label.config(text=f"Is equal to {kms:.2f} Kilometers")

# Create an entry for miles
input = Entry(width=10)
input.grid(row=0, column=1)

# Create label "Miles"
my_label = Label(root, text="Miles", font=("Arial", 12))
my_label.grid(row=0, column=2)

# Create label in the second line
result_label = Label(root, text=f"Is equal to 0 km", font=("Arial", 12))
result_label.grid(row=1, column=1)

# Create and pack a button
button = Button(root, text="Calculate", command=converter)
button.grid(row=2, column=1)

# Start the Tkinter event loop
root.mainloop()