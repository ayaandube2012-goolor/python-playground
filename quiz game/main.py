import random
from question_model import Question
from data import question_data, horrible_result_messages, low_score_messages, good_score_messages, best_score_messagest
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["answer"]
    question_explanation = question["explanation"]
    question_object = Question(question_text, question_answer, question_explanation)
    question_bank.append(question_object)

question_bank = random.sample(question_bank, 10)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have officially completed my general knowledge quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

if quiz.score  < 5:
    print(random.choice(horrible_result_messages))
elif quiz.score < 7:
    print(random.choice(low_score_messages))
elif quiz.score < 10:
    print(random.choice(good_score_messages))
else:
    print(random.choice(best_score_messages))
