def convert(fahrenheit):
    celcius = (fahrenheit - 35) * 5/9
    return "{:>3} F || {:>6.2f} C".format(fahrenheit, celcius)


print(convert(100))
print(convert(56))
print(convert(78))
print(convert(-89))
