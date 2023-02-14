import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain) -> None:

        self.quiz = quiz
        self.window = tkinter.Tk()
        self.window.title('Quiz')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = tkinter.Canvas(width=300, height=250, background='white')
        self.question_text = self.canvas.create_text(150, 125, text="TEXTO AQUI", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.score = tkinter.Label(text='Score: 0', fg='white', background=THEME_COLOR)
        self.score.grid(column=1, row=0)

        true_image = tkinter.PhotoImage(file='images/true.png')
        false_image = tkinter.PhotoImage(file='images/false.png')

        self.true_button = tkinter.Button(image=true_image)
        self.true_button.grid(column=0, row=2)

        self.false_button = tkinter.Button(image=false_image)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
