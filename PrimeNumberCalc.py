print("Prime Number Calculator v1.0\n")

try:
    while True:
        try:
            n = int(input("Zadejte celé číslo: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\nHodnota musí být celé číslo!\n")
            continue

        primeNum = True
        if n < 2:
            primeNum = False
        else:
            for i in range(2, n):
                if n % i == 0:
                    primeNum = False
                    break
        print("Číslo je prvočíslo!\n" if primeNum else "Číslo není prvočíslo!\n")
except KeyboardInterrupt:
    exit(0)