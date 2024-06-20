class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.question_quantity = len(question_list)

    def still_has_questions(self):
        return self.question_number < self.question_quantity

    def next_question(self):

        this_question = self.question_list[self.question_number]
        q = this_question.text
        a = this_question.answer
        h = this_question.category

        if h != 'Uncategorized':
            print(f"[category: {h}]")

        # We need to increment this to get the next question in the next iteration
        self.question_number += 1
        ask = input(f"Q{self.question_number}.: {q} (True/False)?: ").title()
        self.check_answer(ask, a)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct! Well done,", end=" ")
            self.score += 1
        else:
            print(f"That's wrong the right answer is '{correct_answer}',", end=" ")
        print(f"your current score is {self.score}/{self.question_number}\n")

    def game_ends(self):
        print(f"You've completed the quiz!\nYour final score was {self.score}/{self.question_quantity}.")
