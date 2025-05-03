print("Divisibility tester of 5 v1.0\n")

try:
    while True:
        try:
            n = float(input("Zadejte číslo: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\n")
            continue

        if n % 5 == 0:
            print("Číslo je dělitelné pěti!\n")
        else:
            print("Číslo není dělitelné pěti!\n")
except KeyboardInterrupt:
    exit(0)
