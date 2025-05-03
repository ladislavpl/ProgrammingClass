print("Num Checker v1.0\n")

try:
    while True:
        try:
            n = float(input("Zadejte číslo: "))
        except ValueError:
            print("Zadána neplatná hodnota!\n")
            continue

        if n > 10 and n <= 20:
            print("Číslo je v intervalu (10,20>\n")
        else:
            print("Číslo není v intervalu (10,20>\n")
except KeyboardInterrupt:
    exit(0)
