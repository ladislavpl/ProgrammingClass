print("Interval printer v1.0\n")

try:
    while True:
        try:
            min = int(input("Zadejte minimální číslo: "))
            max = int(input("Zadejte maximální číslo: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu. Hodnota musí být celé číslo!\n")
            continue
        for i in range(min, max + 1):
            if i % 2 == 0:
                print(i)
            if i == max:
                print()
except KeyboardInterrupt:
    exit(0)