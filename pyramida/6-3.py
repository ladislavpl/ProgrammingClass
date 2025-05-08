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
except KeyboardInterrupt:
    exit(0)
print(f"Výsledek: {sum(sumArray)}")