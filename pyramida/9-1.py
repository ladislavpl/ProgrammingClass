morse = {
    "a": "·-",
    "b": "-···",
    "c": "-·-·",
    "d": "-··",
    "e": "·",
    "f": "··-·",
    "g": "--·",
    "h": "····",
    "i": "··",
    "j": "·---",
    "k": "-·-",
    "l": "·-··",
    "m": "--",
    "n": "-·",
    "o": "---",
    "p": "·--·",
    "q": "--·-",
    "r": "·-·",
    "s": "···",
    "t": "-",
    "u": "··-",
    "v": "···-",
    "w": "·--",
    "x": "-··-",
    "y": "-·--",
    "z": "--··",
    "0": "-----",
    "1": "·----",
    "2": "··---",
    "3": "···--",
    "4": "····-",
    "5": "·····",
    "6": "-····",
    "7": "--···",
    "8": "---··",
    "9": "----·"
}

print("Morsecode Translator v1.0\n")

try:
    while True:
        text = input("Zadej text: ")

        text = text.lower()
        translatedArray = []
        isWorking = True
        for letter in text:
            if letter == " ":
                translatedArray.append("   ")
                continue
            try:
                translatedArray.append(morse[letter])
            except KeyError:
                print("V zadaném textu je znak který neumím přeložit.\nText musí být bez háčků a čárek a obsahovat pouze znaky anglické abecedy a čísla.\n")
                isWorking = False
                break
            translatedArray.append(" ")
        if isWorking == False:
            continue
        print(f"Překlad: {"".join(translatedArray)}\n")
except KeyboardInterrupt:
    exit(0)
