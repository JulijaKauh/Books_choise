def mysum(*numbers):
    sum_numbers = 0
    for i in numbers:
        sum_numbers += i
    return sum_numbers


print(mysum(1, 2, 3, 4, 5))
print(mysum(10, 222, 33, 44, 55))
print(mysum(3, 4, 5))
print(mysum())
print(mysum(*[1,3,5,7]))

#*args - allows us to pass a variable number of non-keyword arguments to a Python function. 
#In the function, we should use an asterisk (*) before the parameter name to pass a variable number of arguments.
