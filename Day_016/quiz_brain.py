class QuizBrain:

    def __init__(self, q_list):
        self.questions_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.questions_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.questions_number]
        self.questions_number += 1
        user_answer = input(f"Q.{self.questions_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.questions_number}")
        print("\n")