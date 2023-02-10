import random

def guessing_game():
    secret_number = random.randint(0,100)
    max_guesses = 5
    guessing = 0
    print("You have {} guesses. Good luck!".format(max_guesses))

    while True:
        user_number = input("Type a number: ")
        if user_number.isdigit():
            user_number = int(user_number)
        else:
            print("Please type a number next time")
            quit()
        if user_number == secret_number:
            print("Just right. The answer is {}!".format(user_number))
            if guessing == 0:
                print("You got it at first attempt!")
            else:
                print("You got it in {} guesses!".format(secret_number))
            break
        elif user_number > secret_number:
            print("Too high!")
        else:
            print("Too low!")

        guessing += 1
        if guessing == max_guesses:
            print("You did not guess in time. The answer is {}.".format(secret_number))
            break

guessing_game()
