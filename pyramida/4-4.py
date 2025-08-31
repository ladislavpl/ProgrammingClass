print("Six-Times table adder v1.0\n")  # noqa: INP001

vysledek = 0

for i in range(1, 11):
    vysledek = i * 6 + vysledek
    if i == 10:  # noqa: PLR2004
        print(f"Výsledek: {vysledek}")
