class Quiz:

    def __init__(self,text):

        self.text = text
        self.yes = None
        self.no = None

class QuizManager:
    def __init__(self):
        q1 = Quiz("나는 패턴이 좋다. Q2 YES, Q4 No")
        q2 = Quiz("자연 그대로 플라워패턴 Q3 yes Q5 No")
        q3 = Quiz("B타입")
        q3 = Quiz("단색의 부드러운 이불이 좋다 Q3 yes Q5 No")
        q4 = Quiz("동물이 그려짐 Q3 yes Q5 No")
        q5 = Quiz("c타입 Q3 yes Q5 No")
        q7 = Quiz("A타입 Q3 yes Q5 No")
        q8 = Quiz("심플한 단선 패턴 Q3 yes Q5 No")
        q9 = Quiz("D타입 Q3 yes Q5 No")

        q1.yes = q2
        q1.no = q3

    def getFirstQuiz(self):
        return self.start_quiz

class QuizUI:
    def __init__(self):
        self.manager = QuizManager


    def playShow(self, quiz):

        if quiz == None:
            print("THE END")
            return

        answer = input(quiz.text)

        if answer == 'y':
            self.playShow(quiz.yes)
        elif answer == 'n':
            self.playShow(quiz.no)




# current = q1
# while True:
#
#     if current == None:
#         print("END")
#         break
#     answer = input(current.text)
#
#     if answer == 'y':
#         current = current.yes
#     elif answer == 'n':
#         current = current.no