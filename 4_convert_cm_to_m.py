def convert(centimeters):
    meters = centimeters * 0.01
    return "{:>3} cm || {:>6} m".format(centimeters, meters)


print(convert(2))
print(convert(45))
print(convert(100))
print(convert(-89))
