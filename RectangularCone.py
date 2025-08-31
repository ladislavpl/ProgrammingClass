import sys

print("Volume of rectangular cone v1.0\n")

try:
    while True:
        try:
            a = float(input("Zadejte délku strany a: "))
            v = float(input("Zadejte výšku jehlanu v: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\nHodnota musí být číslo!\n")

        print(f"V = {(1 / 3) * a**2 * v}\n")
except KeyboardInterrupt:
    sys.exit(0)
