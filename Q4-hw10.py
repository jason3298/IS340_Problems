from questions import FillinQuestion
q1=FillinQuestion() #create Question and Answer
q1.setText("The inventor of Python was _Guido van Rossum_")
q1.display() #Display the question
re = input('Your answer:')
print(q1.checkAnswer(re)) #check the answer
