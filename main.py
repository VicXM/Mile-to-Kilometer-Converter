from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles_input = float(input_miles.get())
    km_result = miles_input * 1.60934
    label_result.config(text=f"{km_result}")
    
label_miles = Label(text="miles")
label_miles.grid(column=2, row=0)

label_text = Label(text="is equal to")
label_text.grid(column=0, row=1)

label_result = Label(text="0")
label_result.grid(column=1, row=1)

label_km = Label(text="km")
label_km.grid(column=2, row=1)

my_button = Button(text="Calculate", command=miles_to_km)
my_button.grid(column=1, row=2)

input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

window.mainloop()
