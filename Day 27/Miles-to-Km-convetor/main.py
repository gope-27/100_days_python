from tkinter import *

def miles_to_km():
    miles = miles_input.get()
    if miles:  # Check if input is not empty
        km = float(miles) * 1.609
        kilometer_result_label.config(text=f"{km:.2f}")
    else:
        kilometer_result_label.config(text="Invalid input")

# Create the main window
window = Tk()
window.title("Miles to Kilometers Converter")
window.config(pady=20, padx=20)

# Entry for miles input
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Label for "Miles"
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label for "is equal to"
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Label for kilometer result
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Label for "Km"
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Button to calculate
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Start the GUI event loop
window.mainloop()
