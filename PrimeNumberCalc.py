import sys

print("Prime Number Calculator v1.0\n")

try:
    while True:
        try:
            n = int(input("Zadejte celé číslo: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\nHodnota musí být celé číslo!\n")
            continue

        primenum = True
        if n < 2:  # noqa: PLR2004
            primenum = False
        else:
            for i in range(2, n):
                if n % i == 0:
                    primenum = False
                    break
        print("Číslo je prvočíslo!\n" if primenum else "Číslo není prvočíslo!\n")
except KeyboardInterrupt:
    sys.exit(0)
