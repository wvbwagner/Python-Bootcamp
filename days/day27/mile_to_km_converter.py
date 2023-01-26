import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

miles = tkinter.Label(text='miles')
miles.grid(column=4, row=1)
miles.config(padx=5, pady=5)

is_equal = tkinter.Label(text='is equal to')
is_equal.grid(column=2, row=2)
is_equal.config(padx=5, pady=5)

conversion = tkinter.Label(text=0)
conversion.grid(column=3, row=2)
conversion.config(padx=5, pady=5)

km = tkinter.Label(text='km')
km.grid(column=4, row=2)
km.config(padx=5, pady=5)

input = tkinter.Entry(width=8)
input.grid(column=3, row=1)

def calculate():
    kilometers = int(input.get()) * 1.6
    conversion.config(text=kilometers)

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=3, row=3)
button.config(padx=5, pady=5)

window.mainloop()
