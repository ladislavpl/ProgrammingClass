import sys  # noqa: INP001

print("Some Test v1.0\n")

try:
    while True:
        try:
            n = float(input("Zadej číslo: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\n")
            continue

        if n % 5 == 0 and n > 0 and n % 10 != 0:
            print("Číslo splňuje podmínky!\n")
        else:
            print("Číslo nesplňuje podmínky!\n")
except KeyboardInterrupt:
    sys.exit(0)
