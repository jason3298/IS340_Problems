class Question:
    def __init__(self):
        self.text = ''
        self.answer = ''

    #set question
    def setText(self,questionText):
        self.text = questionText
    #set answer
    def setAnswer(self, correctResponse):
        self.answer = correctResponse
    def checkAnswer(self,response):
        return response == self.answer
    #display the question
    def display(self):
        print(self.text)
#MCQ subclass
class MultiChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
    #sort string and check
    def checkAnswer(self,response):
        return sorted(response)== sorted (self.answer)
