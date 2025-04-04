# List of question prompts
question_prompts = [
  "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
  "What color are banana?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
  "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# Custom class question
class question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

# List with the questions and their correct answers
questions = [
  question(question_prompts[0], "a"),
  question(question_prompts[1], "c"),
  question(question_prompts[2], "b"),
]

# Function to run the test
def run_test(questions_list):
  score = 0
  for question in questions_list:
    answer = input(question.prompt)
    if answer == question.answer:
      score = score + 1
  print("You got " + str(score) + "/" +  str(len(questions_list)) + " correct")

# Call function to run the test
run_test(questions)
