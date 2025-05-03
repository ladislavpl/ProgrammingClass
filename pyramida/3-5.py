print("Bigger Num Printer v1.0\n")

try:
    while True:
        try:
            x = float(input("Zadejte 1. číslo: "))
            y = float(input("Zadejte 2. číslo: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\n")
            continue

        if x > y:
            print(f"{x}\n")
        else:
            print(f"{y}\n")
except KeyboardInterrupt:
    exit(0)
    