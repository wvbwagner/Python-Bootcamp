class QuizBrain:
    def __init__(self, q_list) -> None:
        self.q_number = 0
        self.points = 0
        self.question = q_list
        

    def still_has_questions(self):
        self.size = len(self.question)
        if self.q_number < self.size:
            return True 
        return False
        #  poderia ser return self.q_number < self.size

    def next_question(self):
        while self.still_has_questions():
            q_now = self.question[self.q_number]
            self.q_number += 1
            answer = input(f'Q.{self.q_number}: {q_now.text} (True, False) ').strip().capitalize()
            self.check_answer(answer, q_now.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.capitalize():
            self.points += 1
            print(f'You got it right!\nYour score is {self.points}/{self.q_number}')
        else:
            print(f'You\'re wrong! Game over!')
            print(f'The correct answer is {correct_answer}')
            print(f'Your score is {self.points}/{self.q_number}')
            exit(1)


