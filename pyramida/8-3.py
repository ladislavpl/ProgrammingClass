import sys  # noqa: INP001

vowels = "aeiouyáéíóúý"

print("Vowel Counter v1.0\n")

try:
    while True:
        text = input("Zadejte text: ")

        counter = 0
        for letter in text:
            for vowel in vowels:
                if letter == vowel:
                    counter += 1
        print(f"Počet samohlásek: {counter}\n")
except KeyboardInterrupt:
    sys.exit(0)
