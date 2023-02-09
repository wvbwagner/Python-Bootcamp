import requests
import tkinter

window = tkinter.Tk()
window.title('Porra de tkinter de novo...')
window.config(padx=50, pady=50)

def get_stupidness():
    reponse = requests.get(url='https://api.kanye.rest')
    reponse.raise_for_status()
    shit = reponse.json()
    more_shit = shit.get('quote')
    canvas.itemconfig(text, text=more_shit)
    

canvas = tkinter.Canvas(width=300, height=414)
bg = tkinter.PhotoImage(file='background.png')
canvas.create_image(150, 207, image=bg)
text = canvas.create_text(150, 207, text='What(the fuck)ever', width=250, font=('Arial', 20, 'bold'))
canvas.grid(column=0, row=0)

imbecil = tkinter.PhotoImage(file='kanye.png')
button = tkinter.Button(image=imbecil, highlightthickness=0, command=get_stupidness)
button.grid(column=0, row=1)

window.mainloop()
