code_english = {"a": "ф", "b": "и", "c": "с", "d": "в", "e": "у", "f": "а", "g": "п", "h": "р", "i": "ш", 
    "j": "о", "k": "л", "l": "д", "m": "ь", "n": "т", "o": "щ", "p": "з", "q": "й", "r": "к", 
    "s": "ы", "t": "е", "u": "г", "v": "м", "w": "ц", "x": "ч", "y": "н", "z": "я", "A": "Ф", 
    "B": "И", "C": "С", "D": "В", "E": "У", "F": "А", "G": "П", "H": "Р", "I": "Ш", "J": "О", 
    "K": "Л", "L": "Д", "M": "Ь", "N": "Т", "O": "Щ", "P": "З", "Q": "Й", "R": "К", "S": "Ы", 
    "T": "Е", "U": "Г", "V": "М", "W": "Ц", "X": "Ч", "Y": "Н", "Z": "Я", "[":"х", "]":"ъ",
    ";":"ж", ":" : "Ж", "'" : "э", "{": "Х", "}": "Ъ", ",": "б", "<": "Б", ".": "ю", ">": "Ю"}

def translate(text):
    new_text = ""
    for i in text:
        if i in code_english:
            new_text += code_english[i]
        elif i.isdigit():
            new_text += i
        elif i == " ":
            new_text += i
    return new_text
        
print("Enter your message: ")
text = input(">>> ")

print(translate(text))
