print("Welcome to my first quiz!")

start = input("Do you want to play? ")

if start.lower() != "yes":
    print("Ok! See you next time!")
    quit()

print("Great! Let's play! \n")
question = 0
scores = 0

answer = input("What year did The Office (American version) start? ")
if answer.lower() == "2005":
    question += 1
    scores += 10
    print("Well done!")
    print("You got " + str(scores) + " scores. \n")
else:
    print("Incorrect. \n")

answer = input("Whats the name of the company The Office employees work for? ")
if answer.lower() == "dunder mifflin":
    question += 1
    scores += 10
    print("Well done!")
    print("You got " + str(scores) + " scores. \n")
else:
    print("Incorrect. \n")

answer = input("What’s the company's annual award ceremony called? ")
if answer.lower() == "the dundies":
    question += 1
    scores += 10
    print("Well done!")
    print("You got " + str(scores) + " scores. \n")
else:
    print("Incorrect. \n")

print("You answered correctly " + str(question) + " questions, and you got " + str(scores) + " scores!")
