def caesar(text, offset):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    text = text.lower()
    toArray = list(text)
    tempArray = []

    for i in range(len(toArray)):
        temp = alphabet.index(toArray[i])
        temp += offset
        while temp > 25:
            temp -= 26
        while temp < 0:
            temp += 26
        tempArray.append(alphabet[temp])
    
    return "".join(tempArray)

print(caesar("yfmh", -50))