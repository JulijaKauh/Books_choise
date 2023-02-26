import random

user_scores = 0
computer_scores = 0


options = ["rock", "paper", "scissors"]

while True:   
    user_option = input("Type rock, paper or scissors if you want to play, or type Q to quit: ").lower()
    if user_option == "q":
        quit()
    elif user_option not in options:
        continue

    random_number = random.randint(0,2)
    computer_option = options[random_number]

    if user_option == "rock" and computer_option == "scissors":
        print("You won! Rock wins against scissors")
        user_scores += 1
        print("You {} -- {} Computer".format(user_scores, computer_scores))
        
    elif user_option == "paper" and computer_option == "rock":
        print("You win! Paper wins against rock")
        user_scores += 1
        print("You {} -- {} Computer".format(user_scores, computer_scores))

    elif user_option == "scissors" and computer_option == "paper":
        print("You won! Scissors wins against paper")
        print("You {} -- {} Computer".format(user_scores, computer_scores))
        user_scores += 1

    elif user_option == computer_option:
        print("Tie")
        print("You {} -- {} Computer".format(user_scores, computer_scores))
        continue
    else:
        print("You lose")
        computer_scores += 1
        print("You {} -- {} Computer".format(user_scores, computer_scores))

print("Your scores: ", user_scores, ". Computer scores: ", computer_scores)
