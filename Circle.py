from math import pi

print("Obvod a obsah kružnice v1.0\nProgram používá pi přesné na 15 desetinných míst")

try:
    while True:
        try:
            r = float(input("Zadej poloměr r: "))
        except ValueError:
            print("Invalidní hodnota!\n")
            continue
        print(f"o = {2 * r * pi}\nS = {pi * r ** 2}\n")
except KeyboardInterrupt:
    exit(0)