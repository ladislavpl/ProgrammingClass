import sys  # noqa: INP001

print("kebab-case to UPPER_SNAKE_CASE Converter v1.0\n")

try:
    while True:
        text = input("Zadejte text v podobě kebab-case: ")

        text = text.upper()
        convertedList = []
        for letter in text:
            if letter == "-":
                convertedList.append("_")
            else:
                convertedList.append(letter)
        print("".join(convertedList))
except KeyboardInterrupt:
    sys.exit(0)
