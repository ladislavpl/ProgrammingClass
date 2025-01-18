import random

print("Number Guessing Game version Beta\n")
print("Hádáš číslo mezi 1 - 9.\nNa uhodnutí čísla máš tři pokusy.\nPokud neuhodneš, vygeneruje se číslo nové.\n")
try:
    while True:
        randomInt = random.randint(1, 9)
        try:
            for i in range(3):
                guess = int(input("Hádej číslo: "))

                if randomInt == guess:
                    print("Gratuluji! Číslo jsi uhodl.\n")
                    break
                elif guess >= 10 or guess <= 0:
                    print("Číslo je neplatné! Neplýtvej pokusy. :)\n")
                else:
                    print("Číslo jsi neuhodl!\n")
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\n")
        print("Generuji nové číslo.\n")
except KeyboardInterrupt:
    exit(0)
    