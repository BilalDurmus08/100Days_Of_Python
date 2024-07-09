class QuizBrain:

    def __init__(self, question_l):
        self.question_number = 0
        self.question_list = question_l
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer1 = input(f"\n{self.question_number + 1} : {current_question.text}. (True or False): ")
        self.question_number += 1
        self.check_answer(answer1, current_question.answer)

    def still_has_a_question(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, answer, corrct_answer):
        if answer == corrct_answer:
            print("Congrats Correct answer!")
            self.score += 1
        else:
            print("You piece of lazy you are wrong!")
        print(f"The correct answer is: {corrct_answer}")
        print(f"The score is: {self.score}/{self.question_number}")
