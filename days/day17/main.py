from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []


for item in question_data:
    text = item['text']
    answer = item['answer']
    new_question = Question(text=text, answer=answer)
    question_bank.append(new_question)


q1 = QuizBrain(question_bank)
q1.next_question()
     