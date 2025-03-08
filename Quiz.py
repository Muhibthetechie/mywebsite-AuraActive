import random
class FruitQuiz:
    def __init__(self):
        self.fruit = {'Apple':'red','Banana':'yellow','Orange':'Orange','Mango':'yellow'}
    def quiz(self):
        while True:
            fruit , color = random.choice(list(self.fruit.items()))
            print("What is the color of fruit {}", format(fruit))
            user_answer = input()

            if(user_answer.lower() ==color):
                print("Correct answer")
            else:
                print("Wrong answer")
            option = int(input("Enter 0 to quit or 1 to play further:"))
            if (option):
                break
print("This is fruit quiz")
fq = FruitQuiz()
fq.quiz()
