print("Word Flip v1.0\n")
try:
    while True:
        word = list(input("Zadej slovo: "))
        word.reverse()
        print(f"Výsledek: {"".join(word)}\n")
except KeyboardInterrupt:
    exit(0)
