import sys

print("""Right-angled triangle tester v1.0

      Zadáte tři strany (nezáleží na pořadí ani délce).
      Program vypíše, zda je trojuhelník pravoúhlý.
      """)

try:
    while True:
        try:
            sides = [float(input(f"Zadej {i}. stranu: ")) for i in range(1, 4)]
        except ValueError:
            print("Zadána neplatná hodnota!\n")
            continue

        if sides[0] > sides[1] and sides[0] > sides[2]:
            c = sides[0]
            result = sides[1] ** 2 + sides[2] ** 2
        elif sides[1] > sides[0] and sides[1] > sides[2]:
            c = sides[1]
            result = sides[0] ** 2 + sides[2] ** 2
        elif sides[2] > sides[1] and sides[2] > sides[0]:
            c = sides[2]
            result = sides[0] ** 2 + sides[1] ** 2

        if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            print("Trojuhelník není pravoúhlý\n")
        elif c**2 == result:
            print("Trojuhelník je pravoúhlý\n")
        else:
            print("Trojuhelník není pravoúhlý\n")
except KeyboardInterrupt:
    sys.exit(0)
