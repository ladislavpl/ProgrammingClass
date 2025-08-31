import sys
from random import randint

print("Number Guessing Game v1.0\n")
print("""Hádáš číslo mezi 1 - 9.
      Na uhodnutí čísla máš tři pokusy.\nPokud neuhodneš, vygeneruje se číslo nové.
      """)
try:
    while True:
        randomint = randint(1, 9)  # noqa: S311
        for _ in range(3):
            try:
                guess = int(input("Hádej číslo: "))

                if randomint == guess:
                    print("Gratuluji! Číslo jsi uhodl.\n")
                    break
                elif guess >= 10 or guess <= 0:  # noqa: PLR2004
                    print("Číslo je neplatné! Neplýtvej pokusy. :)\n")
                elif guess > randomint:
                    print("Vaše číslo je větší než to správné\n")
                elif guess < randomint:
                    print("Vaše číslo je menší než to správné\n")
            except ValueError:
                print("Zadali jste neplatnou hodnotu!\n")
        print("Generuji nové číslo.\n")
except KeyboardInterrupt:
    sys.exit(0)
