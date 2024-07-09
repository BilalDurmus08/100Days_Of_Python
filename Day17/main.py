from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_model1 = Questions(question["text"], question["answer"])
    question_bank.append(question_model1)

quiz_brain_o = QuizBrain(question_bank)

while quiz_brain_o.still_has_a_question():
    quiz_brain_o.next_question()
