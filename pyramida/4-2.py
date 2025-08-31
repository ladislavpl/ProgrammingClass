import sys  # noqa: INP001

print("Interval printer v1.0\n")

try:
    while True:
        try:
            minimum = int(input("Zadejte minimální číslo: "))
            maximum = int(input("Zadejte maximální číslo: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu. Hodnota musí být celé číslo!\n")
            continue
        for i in range(minimum, maximum + 1):
            if i % 2 == 0:
                print(i)
            if i == maximum:
                print()
except KeyboardInterrupt:
    sys.exit(0)
