import sys  # noqa: INP001

print("Remainder after division v1.0\n")

try:
    while True:
        try:
            x = int(input("Zadej 1. číslo: "))
            y = int(input("Zadej 2. číslo: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\nHodnota musí být celé číslo.\n")
            continue
        if x < 0:
            operatorX = "-"
            x *= -1
        else:
            operatorX = "+"
        if y < 0:
            operatorY = "-"
            y *= -1
        elif y > 0:
            operatorY = "+"
        else:
            print("Nulou nelze dělit!\n")
            continue
        vysledek = 0
        while vysledek < x:
            vysledek += y
        if vysledek != x:
            vysledek -= y
        if (operatorX == "-" and operatorY == "+") or (
            operatorX == "+" and operatorY == "-"
        ):
            zbytek = (x - vysledek) * -1
        else:
            zbytek = x - vysledek
        print(f"Zbytek: {zbytek}\n")
except KeyboardInterrupt:
    sys.exit(0)
