import random

max_number = input("Please type a number: ")

if max_number.isdigit():
    max_number = int(max_number)
    if max_number <= 0:
        print("Please type a number larger than 0!")
        quit()
else:
    print("Please type a number next time!")
    quit()


random_number = random.randint(0, max_number)
guesses = 0

while True:
    guesses += 1
    user_number = input("Make a guess: ")
    if user_number.isdigit():
       user_number = int(user_number)
    else:
        print("Type a number")
        continue

    if random_number == user_number:
           print("Great you got it! The number was:", random_number, "!")
           break
    elif user_number > random_number:
            print("Your number is too big")
    else:
            print("Your number is to small")

print("You got it in", guesses, "guesses!")
