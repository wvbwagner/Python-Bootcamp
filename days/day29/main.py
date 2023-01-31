import tkinter
import string
import pyperclip
from random import randint, choice
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_generate():
    passwd = ''
    pass_size = randint(8, 15)
    for n in range(pass_size):
        passwd += choice(string.printable).strip()
    generated_pass.insert(0, passwd)
    pyperclip.copy(passwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_to_file():

    text_1 = web_input.get().title()
    text_2 = user.get()
    text_3 = generated_pass.get()
    if len(text_1) > 0 and len(text_3) > 0:
        confirmation = messagebox.askokcancel(title=text_1, 
        message=(f'Are you sure you want to save?'))
        if confirmation:
            with open ('data.txt', mode = 'a') as data:
                data.write(f'{text_1} | {text_2} | {text_3}\n')
                web_input.delete(0, len(text_1))
                generated_pass.delete(0, len(text_3))
        elif not confirmation:
            generated_pass.delete(0, len(text_3))
    elif len(text_1) == 0:
        messagebox.showerror(title="Error", message="Website can not be empty")
    elif len(text_3) == 0:
        messagebox.showerror(title="Error", message="Password can not be empty")

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
locker = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=locker)
canvas.grid(column=1, row=0)

#LABELS

website = tkinter.Label(text="Website:")
website.grid(column=0, row=1)

username = tkinter.Label(text="Email/Username:")
username.grid(column=0, row=2)

password = tkinter.Label(text="Password:")
password.grid(column=0, row=3)

#INPUTS

web_input = tkinter.Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus() #coloca o cursor neste input


user = tkinter.Entry(width=35)
user.grid(column=1, row=2, columnspan=2)
user.insert(0, 'wagner.botelho@gmail.com')


generated_pass = tkinter.Entry(width=24)
generated_pass.grid(column=1, row=3)

#BUTTONS
    
generate = tkinter.Button(text="Generate\nPassword", font=('Arial', 9, 'normal'), command=pass_generate)
generate.grid(column=2, row=3)

adding = tkinter.Button(text="Add", width=32, command=add_to_file)
adding.grid(column=1, row=4, columnspan=2)

window.mainloop()