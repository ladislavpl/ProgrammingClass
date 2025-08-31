import sys  # noqa: INP001

print("Abs v1.0\n")

try:
    while True:
        try:
            n = float(input("Zadejte číslo: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\n")
            continue

        print(f"Absolutní hodnota je: {abs(n)}\n")
except KeyboardInterrupt:
    sys.exit(0)
