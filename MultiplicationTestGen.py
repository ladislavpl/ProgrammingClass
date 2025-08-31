import sys
from random import randint

print("Multiplication Test Generator v1.0\n")

try:
    while True:
        problem = [randint(1, 10), randint(1, 10)]  # noqa: S311
        correctresult = problem[0] * problem[1]

        try:
            userresult = int(input(f"{problem[0]} * {problem[1]} = "))
        except ValueError:
            print(f"""Zadali jste neplatnou hodnotu!
                  Správný výsledek je: {correctresult}
                  """)
            continue

        if userresult == correctresult:
            print("Výsledek je správný!\n")
        else:
            print(f"Výsledek je špatně!\nSprávný výsledek je: {correctresult}\n")
except KeyboardInterrupt:
    sys.exit(0)
