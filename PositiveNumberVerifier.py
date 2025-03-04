print("Verifikátor kladných čísel v1.0\nProgram ověří jestli je zadané číslo kladné.\n")

try:
    while True:
        try:
            n = float(input("Zadej číslo: "))
        except ValueError:
            print("Zadána invalidní hodnota!\n")
            continue
        print(f"Výsledek: {n > 0}\n")
except KeyboardInterrupt:
    exit(0)