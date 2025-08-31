import sys
from random import choices

validcolors = "RBYGWOP"
print("Mastermind v1.0\n")

def count_correct(code, guess):
    correction = []
    for j in range(len(code)):
        correction.append("")
        for k in range(len(guess)):
            if k == j and code[j] == guess[k]:
                correction[j] = "W"
            elif guess[k] == code[j] and correction[j] == "":
                correction[j] = "B"
    correction = [j for j in correction if j != ""]
    correction.sort(reverse=True)
    print(f"Výsledek: {" ".join(correction)}\n")
    return correction.count("W") == 6  # noqa: PLR2004

def play():
    win = False
    code = []
    code = choices(validcolors, k=6)  # noqa: S311
    print("""Výběr barev:
          R - červená
          B - modrá
          Y - žlutá
          G - zelená
          W - bílá
          O - orandžová
          P - růžová
          Pokusy zadávejte bez mezer, 6 barev
          """)
    i = 0
    while i < 10:  # noqa: PLR2004
        guess = input(f"Pokus č.{i + 1}: ")
        if len(guess) == 6:  # noqa: PLR2004
            if set(guess).issubset(set(validcolors)):
                win = count_correct(code, guess)
                if win:
                    break
                i += 1
            else:
                print("Zadali jste neplatnou hodnotu!")
                continue
        elif len(guess) < 6:  # noqa: PLR2004
            print("Zadali jste málo barev!\n")
            continue
        else:
            print("Zadali jste moc barev!\n")
            continue
    if win:
        print("Uhodl jsi!\n")
    else:
        print("Neuhodl jsi :D\n")



try:
    while True:
        exitorplay = input("Zadejte play nebo exit: ")
        if exitorplay.strip().lower() == "exit":
            sys.exit(0)
        elif exitorplay.strip().lower() == "play":
            play()
        else:
            print("Neplatná hodnota!\n")
except KeyboardInterrupt:
    sys.exit(0)
