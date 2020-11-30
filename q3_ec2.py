#  This program shows a simple quiz with one question.
from EC2 import MultiChoiceQuestion
# Create the question and expected answer.
q = MultiChoiceQuestion()
q.setText("Of Apple, Tomato, Carrot, Cucumber and Celery, list all that are fruit.")
q.setAnswer("Apple Tomato")      

# Display the question and obtain user's response (Apple Tomato).
q.display()
response = input("Your answer: ")
print(q.checkAnswer(response)) 

# Display the question and obtain user's response (Tomato Apple).
q.display()
response = input("Your answer: ")
print(q.checkAnswer(response))

# Display the question and obtain user's response (Carrot).
q.display()
response = input("Your answer: ")
print(q.checkAnswer(response))



