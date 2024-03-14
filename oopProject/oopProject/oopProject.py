class Questions:
    def __init__(self,question,choose,answer):
        self.question=question
        self.choose=choose
        self.answer=answer

class Quiz(Questions):
    def __init__(self, question, choose, answer,no):
        super().__init__(question, choose, answer)
        self.questionNumber=no
        
    def startQuiz(self):
        global score
        print(f'Question number {self.questionNumber} of 3\n\n{self.question}{self.choose}')
        userChoose=input('\nanswer: ')
        print('\n')
        if userChoose==self.answer:
            score=score+1
score=0        
q1=Quiz('What is the best programing language ?','\n-java\n-c++\n-c#','java',1)
q2=Quiz('What is the easy programing language?','\n-java\n-c++\n-python','python',2)
q3=Quiz('What is the hard programing language?','\n-java\n-c\n-c#','c#',3)
questionList=[q1,q2,q3]
for i in questionList:
    i.startQuiz()

print('score: {0}'.format(score))