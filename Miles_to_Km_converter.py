import tkinter

def mile2km():
    miles = float(miles_input.get())
    km = miles*1.609
    km_results_label.config(text=km)


# window creation
window = tkinter.Tk()
window.minsize(height=150, width=350)
window.title("Miles to Km Converter")
window.config(padx=100, pady=100)


# Input Box
miles_input = tkinter.Entry(width=6)
miles_input.get()
miles_input.grid(column=1, row=0)



# label creation

Miles_label = tkinter.Label(text="Miles")
Miles_label.grid(row=0, column=2)

is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km_results_label = tkinter.Label(text="0")
km_results_label.grid(row=1, column=1)

Km_label = tkinter.Label(text="Km")
Km_label.grid(row=1, column=2)


# Button creation
button = tkinter.Button(text="Calculate", command=mile2km)
button.grid(column=1, row=2)


window.mainloop()