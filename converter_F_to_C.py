def converter(fahrenheit):
    celcius = (fahrenheit - 35) * 5/9
    return "{:>3} F || {:>6.2f} C".format(fahrenheit, celcius)


print(converter(100))
print(converter(56))
print(converter(78))
print(converter(-89))
