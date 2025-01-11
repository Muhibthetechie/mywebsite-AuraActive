import random
playing = True
number = str(random.randint(10,20))

print("I will print a number from 0 to 9 , you have to guess it one by one.")
print("The game end when you get 1 hero!")
while playing:
    guess = input("Give me your best guess. \n")
    if number == guess:
        print("You won!")
        print("The number was", number)
        break
else:
    print("Your guess wasnt quiet correct try again.\n")