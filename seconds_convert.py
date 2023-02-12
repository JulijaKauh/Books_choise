def second_convert(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds -  hours * 3600 - minutes * 60

    return "{} seconds: {} hours, {} minutes, {} seconds". format(seconds, hours, minutes, remaining_seconds)

print(second_convert(2000))
print(second_convert(50))
print(second_convert(80900))
print(second_convert(2000))
print(second_convert(50))
print(second_convert(1440))
