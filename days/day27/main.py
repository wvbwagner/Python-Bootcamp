import tkinter

window = tkinter.Tk()
window.title('Shown at the top')
window.minsize(width= 500, height= 300)

label = tkinter.Label(text="I am a label")
label.grid(column=0, row=0)


def button_clicked():
    label.config(text=input.get())

button = tkinter.Button(text='Click me', command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text='New button')
new_button.grid(column=2, row=0)

input = tkinter.Entry(width=8)
input.grid(column=3, row=2)


window.mainloop()