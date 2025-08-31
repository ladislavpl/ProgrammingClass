import sys  # noqa: INP001

print("BMI Calculator v1.0")

try:
    while True:
        try:
            m = float(input("Zadejte vaši váhu v kg: "))
            h = float(input("Zadejte vaši výšku v cm: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu. Opakujte akci znovu!\n")
            continue

        BMI = m / (h / 100) ** 2

        print(f"Vaše BMI je: {BMI}\n")
except KeyboardInterrupt:
    sys.exit(0)
