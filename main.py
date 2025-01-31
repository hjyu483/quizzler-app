from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface




question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question) # put everything in question model and it is included in list


quiz = QuizBrain(question_bank) # put list on a string to class now quiz is class in question_model


# while quiz.still_has_questions(): #quiz.still has questions
#     quiz.next_question()
quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
