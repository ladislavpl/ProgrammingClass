import sys  # noqa: INP001
from math import pi

print("Circle Calc v1.0\n")

try:
    while True:
        try:
            r = float(input("Zadejte poloměr r: "))
        except ValueError:
            print("Zadána neplatná hodnota\n")
            continue
        obvod = 2 * pi * r
        obsah = pi * r**2

        print(f"Obvod: {obvod}\nObsah: {obsah}\n")
except KeyboardInterrupt:
    sys.exit(0)
