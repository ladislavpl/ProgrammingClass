import sys  # noqa: INP001

print("Positive Number Tester v1.0")

try:
    while True:
        try:
            n = float(input("Zadejte číslo: "))
        except ValueError:
            print("Zadána neplatná hodnota!\n")
            continue
        if n > 0:
            print("Ano\n")
        elif n <= 0:
            print("Ne\n")
except KeyboardInterrupt:
    sys.exit(0)
