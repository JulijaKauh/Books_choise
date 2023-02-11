def converter(centimeters):
    meters = centimeters * 0.01
    return "{:>3} cm || {:>6} m".format(centimeters, meters)


print(converter(2))
print(converter(45))
print(converter(100))
print(converter(-89))
