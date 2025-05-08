alphabet = "abcdefghijklmnopqrstuvwxyz"

print("Caesar Shift v1.1\n")

try:
    while True:
        text = input("Zadejte text, který chcete zašifrovat: ")
        try:
            offset = int(input("Zadejte offset: "))
        except ValueError:
            print("Zadána neplatná hodnota! Offset musí být celé číslo.\n")
            continue

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
except KeyboardInterrupt:
    exit(0)