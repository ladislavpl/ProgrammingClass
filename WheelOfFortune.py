from random import choice

print("Kolo štěstí v1.0\n")

try:
    while True:
        kolostesti = []
        print("Zadej text, který chceš přidat do kola. Pokud jsi skončil, zadej !")
        while True:
            temp = input()
            if temp == "!":
                break
            else:
                kolostesti.append(temp)
        if kolostesti != []:
            print("\nVýsledek: " + choice(kolostesti) + "\n")
        else:
            print("\nNezadali jste žádný text. Kolo nelze spustit!\n")
except KeyboardInterrupt:
    exit(0)