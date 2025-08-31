import sys  # noqa: INP001

print("Chessboard Generator v1.0\n")

if len(sys.argv) > 2:  # noqa: PLR2004
    print("Zadali jste více argumentů než je požadováno!")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except IndexError:
    print("""Nezadali jste argument velikosti šachovnice!
          Syntaxe: python 5-2.py velikost""")
    sys.exit(1)
except ValueError:
    print("Jako argument jste uvedli neplatnou hodnotu!\nArgument musí být celé číslo!")
    sys.exit(2)

if n <= 0:
    print("Nelze vytvořit šachovnici\nVelikost musí být větší než 0!")
    sys.exit(2)

color = 0

for _y in range(n):
    for _x in range(n):
        print(color, end="")
        color = 1 if color == 0 else 0
    if n % 2 == 0:
        color = 1 if color == 0 else 0
    print()
