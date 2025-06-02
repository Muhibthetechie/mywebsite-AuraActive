import random
while True:
    user_input = input("Chose one of the options(rock , paper , scissors):")
    posible_actions = ["rock , paper , sissors"]
    computer_input = random.choice(posible_actions)
    print(f"You chose {user_input} and the computer chose{computer_input}.\n")
    if user_input == computer_input:
        print("Both you and the opponent had the same action {user_action}. Its a Tie!")
    elif computer_input == "sissors":
        user_input == "rock"
        print("You won!")
    elif user_input =="paper":
        computer_input ==