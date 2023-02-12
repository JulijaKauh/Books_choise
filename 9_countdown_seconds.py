def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0: # Complete the while loop
            return_string += str(x) # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -=1 # Decrement the appropriate variable
    else:
        return_string = "Can’t count down to 0"
    return return_string

print("How many seconds to count down?")
start = input()
while not start.isdigit():
    print("How many seconds to count down? Please enter an integer number!")
    start = input()
start = int(start)

print(countdown(start)) 
