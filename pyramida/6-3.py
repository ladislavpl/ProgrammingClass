import sys  # noqa: INP001

print("Sum v1.0\n")

sumArray = []
try:
    while True:
        try:
            n = float(input("Zadejte číslo: "))
        except ValueError:
            print("Zadána neplatná hodnota!")
            continue

        if n == 0:
            break
        else:
            sumArray.append(n)
    print(f"Výsledek: {sum(sumArray)}")
except KeyboardInterrupt:
    sys.exit(0)
