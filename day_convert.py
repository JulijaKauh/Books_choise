def day_convert(day):
    hours = day * 24
    minutes = day * 1440
    seconds = day * 86400
    return "In {} day/s: hours = {}, minutes = {}, seonds = {}".format(day, hours, minutes, seconds)

print(day_convert(7))
print(day_convert(2))
print(day_convert(1))
