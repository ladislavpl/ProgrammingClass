import random

print("Number Guessing Game v1.0\n")
print("Hádáš číslo mezi 1 - 9.\nNa uhodnutí čísla máš tři pokusy.\nPokud neuhodneš, vygeneruje se číslo nové.\n")
try:
    while True:
        randomInt = random.randint(1, 9)
        for i in range(3):
            try:
                guess = int(input("Hádej číslo: "))

                if randomInt == guess:
                    print("Gratuluji! Číslo jsi uhodl.\n")
                    break
                elif guess >= 10 or guess <= 0:
                    print("Číslo je neplatné! Neplýtvej pokusy. :)\n")
                elif guess > randomInt:
                    print("Vaše číslo je větší než to správné\n")
                elif guess < randomInt:
                    print("Vaše číslo je menší než to správné\n") 
            except ValueError:
                print("Zadali jste neplatnou hodnotu!\n")   
        print("Generuji nové číslo.\n")
except KeyboardInterrupt:
    exit(0)
    