from tkinter import *

def calculate():
    km_input = float(user_km_input.get())
    miles_output = km_input * 0.621371
    miles_value.config(text=miles_output)

window = Tk()
window.config(padx=50, pady=30)

user_km_input = Entry(width=10)
user_km_input.grid(row=0, column=1)

km = Label(text="km")
km.grid(row=0, column=2)

equals = Label(text="=")
equals.grid(row=1, column=0)

miles_value = Label(text="0")
miles_value.grid(row=1, column=1)

miles = Label(text="miles")
miles.grid(row=1, column=2)

calculate_button = Button(text="calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()
