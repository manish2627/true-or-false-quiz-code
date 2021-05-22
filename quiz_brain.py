
class QuizBrain():
  def __init__(self, question_list):
    self.question_number = 0
    self.list = question_list
    self.score = 0
  
  def check_answer(self,user_answer,correct_answer):
    if user_answer.lower() == correct_answer.lower():
      print("you are right ")
      self.score += 1
    else:
      print("you are wrong")  
      self.score = self.score
    print(f"the right answer is {correct_answer }")  
    print(f"your current score is {self.score}")
    print("\n ")


  def next_question(self):
    curent_quetion = self.list[self.question_number].text
    self.question_number +=1

    user_answer = input( f"Q.{self.question_number} {curent_quetion} ? (true/false) : ")
    self.check_answer(user_answer, curent_quetion.answer)

  def still_have_question(self):
 
    if self.question_number == len(self.list):
      return False
    else:
      return True

  