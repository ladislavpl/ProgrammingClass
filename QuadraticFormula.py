import sys
from math import sqrt

print("Quadratic Formula Calc v1.0\n")

try:
    while True:
        try:
            a = float(input("Zadej a: "))
            b = float(input("Zadej b: "))
            c = float(input("Zadej c: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\n")
            continue

        D = b**2 - 4 * a * c

        if D < 0:
            print("Není řešení\n")
        elif D == 0:
            x = (-b) / (2 * a)
            print(f"x = {x}\n")
        elif D > 0:
            x1 = (-b - sqrt(D)) / (2 * a)
            x2 = (-b + sqrt(D)) / (2 * a)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}\n")
except KeyboardInterrupt:
    sys.exit(0)
