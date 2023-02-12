def count_char(text):
    result = {}
    for char in text:
        if char.isalpha():
            if char not in result:
                result[char] = 0
            result[char] += 1
        elif char.isdigit():
            if char not in result:
                result[char] = 0
            result[char] += 1
    return result

print(count_char("aaaaaAAAAAA11111222333"))
