import sys

print("Linear Equations Calc v1.0")

try:
    while True:
        try:
            a = float(input("Zadejte koeficient a: "))
            b = float(input("Zadejte koeficient b: "))
        except ValueError:
            print("Zadána neplatná hodnota!\nHodnota musí být reálné číslo!\n")
            continue

        if a == 0 and b == 0:
            print("Nekonečně mnoho řešení!\n")
            continue
        if a == 0:
            print("Nemá řešení!\n")
            continue
        print(f"x = {b * -1 / a}\n")
except KeyboardInterrupt:
    sys.exit(0)
