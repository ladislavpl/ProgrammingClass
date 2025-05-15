from random import randint

print("Multiplication Test Generator v1.0\n")

try:
    while True:
        problem = [randint(1, 10), randint(1, 10)]
        correctResult = problem[0] * problem[1]

        try:
            userResult = int(input(f"{problem[0]} * {problem[1]} = "))
        except ValueError:
            print(f"Zadali jste neplatnou hodnotu!\nSprávný výsledek je: {correctResult}\n")
            continue

        if userResult == correctResult:
            print("Výsledek je správný!\n")
        else:
            print(f"Výsledek je špatně!\nSprávný výsledek je: {correctResult}\n")
except KeyboardInterrupt:
    exit(0)