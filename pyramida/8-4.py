alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

print("Caesar Shift v1.0\n")

while True:
    text = input("Zadejte text, který chcete zašifrovat: ")
    try:
        offset = int(input("Zadejte offset: "))
    except ValueError:
        print("Zadána neplatná hodnota! Offset musí být celé číslo.\n")

    text = text.lower()
    toArray = list(text)
    tempArray = []

    for i in range(len(toArray)):
        try:
            temp = alphabet.index(toArray[i])
        except ValueError:
            tempArray.append(toArray[i])
            continue
        temp += offset
        while temp > 25:
            temp -= 26
        while temp < 0:
            temp += 26
        tempArray.append(alphabet[temp])

    encrypted = "".join(tempArray)

    print(f"Zašifrovaný text: {encrypted}\n")