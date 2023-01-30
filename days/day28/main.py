import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
cicle = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global cicle
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    label.config(text="Timer")
    check.config(text="")
    cicle = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_count():
    global cicle
    marks = ''
    cicle += 1
    print_marks = cicle // 2
    for n in range(print_marks):
        marks += '✔️'
        check.config(text=marks)
    if cicle > 8:
        reset()
    elif cicle == 8:
        label.config(text="Long Break", foreground=RED, background=YELLOW)
        count_down(LONG_BREAK_MIN)
    elif cicle % 2 == 1:
        label.config(text="Work", foreground=GREEN, background=YELLOW)
        count_down(WORK_MIN)   
    elif cicle % 2 == 0:
        label.config(text="Break", foreground=PINK, background=YELLOW)
        count_down(SHORT_BREAK_MIN)  

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = count // 60
    if minutes < 10:
        minutes = f'0{minutes}'
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'
    canvas.itemconfig(timer_text, text=(f'{minutes}:{seconds}'))
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count < 0:
        start_count()
       
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("The Pomodoro Method")
window.config(padx=100, pady=50, bg=YELLOW)

label = tkinter.Label(text='Timer', font=(FONT_NAME, 40, 'bold'))
label.config(bg=YELLOW, highlightthickness=0,foreground=GREEN )
label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_tmt = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_tmt)
timer_text = canvas.create_text(100, 128, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

button_1 = tkinter.Button(text='Start', highlightthickness=0, command=start_count)
button_2 = tkinter.Button(text='Reset', highlightthickness=0, command=reset)
button_1.grid(column=0,row=3)
button_2.grid(column=3, row=3)

check = tkinter.Label (foreground=GREEN, background=YELLOW)
check.grid(column=1, row=4)

window.mainloop()
