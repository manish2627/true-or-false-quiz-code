from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []


for question in question_data:
  new_ques_text = question["text"]
  new_ques_answer = question["answer"]
  new_question = Question(new_ques_text, new_ques_answer)
  question_bank.append(new_question)


next_question = QuizBrain(question_bank)

while next_question.still_have_question():
   next_question.next_question()
final_answer = next_question.score  
print(f"You complete the quiz Your final score is : {final_answer}")
