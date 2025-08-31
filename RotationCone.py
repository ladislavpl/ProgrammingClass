import sys
from math import pi

print("Volume of the rotating cone v1.0\n")

try:
    while True:
        try:
            r = float(input("Zadej poloměr podstavy r: "))
            v = float(input("Zadej výšku kužele v: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\nHodnota musí být číslo!\n")

        print(f"V = {(1 / 3) * (pi * r**2) * v}\n")
except KeyboardInterrupt:
    sys.exit(0)
