from question_model import Question
from data import question_data
from data import opentdb_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = Question(item['text'], item['answer'])
    # print(question.text, ":", question.answer)
    question_bank.append(question)

random_api_questions = []

for q in opentdb_data:
    question = Question(q['question'], q['correct_answer'], q['category'])
    random_api_questions.append(question)

quizz = QuizBrain(random_api_questions)
while quizz.still_has_questions():
    quizz.next_question()
quizz.game_ends()

# This is a list of Question objects
print(question_bank)
print(len(question_bank))
brain = QuizBrain(question_bank)

# while brain.question_number < brain.question_quantity:
while brain.still_has_questions():
    brain.next_question()
brain.game_ends()
