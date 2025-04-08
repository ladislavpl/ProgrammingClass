print("How much percent v1.0")
print("Tento program spočítá kolik je x procent z hodnoty n\n")

try:
    while True:
        try:
            n = float(input("Zadejte hodnotu n: "))
            x = float(input("Zadejte hodnotu x: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu. Opakujte akci znovu!")
            continue
        result = n / (x / 100)

        print(f"Výsledek: {result}%\n")
except KeyboardInterrupt:
    exit(0)