from questions import ChoiceQuestion
def main():
    first = ChoiceQuestion()
    first.setText('In what ye?')
    first.addChoice('1991',True)
    first.addChoice('123',False)
    first.addChoice('123',False)
    first.addChoice('123',False)
    presentQuestion(first)
def presentQuestion(q):
    q.display()
    re = input('ur answer')
    print(q.checkAnswer(re))
main()
    
