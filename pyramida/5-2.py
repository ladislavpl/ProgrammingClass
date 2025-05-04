from sys import argv

print("Chessboard Generator v1.0\n")

if len(argv) > 2:
    print("Zadali jste více argumentů než je požadováno!")
    exit(1)

try:
    n = int(argv[1])
except IndexError:
    print("Nezadali jste argument velikosti šachovnice!\nSyntaxe: python 5-2.py velikost")
    exit(1)
except ValueError:
    print("Jako argument jste uvedli neplatnou hodnotu!\nArgument musí být celé číslo!")
    exit(2)

if n <= 0:
    print("Nelze vytvořit šachovnici\nVelikost musí být větší než 0!")
    exit(2)

color = 0

def colorChange():
    global color
    if color == 0:
        color = 1
    else:
        color = 0

for y in range(n):
    for x in range(n):
        print(color, end="")
        colorChange()
    if n % 2 == 0:
        colorChange()
    print()