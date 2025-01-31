print("Right-angled triangle tester v1.0\n\nZadáte tři strany (nezáleží na pořadí ani délce).\nProgram vypíše, zda je trojuhelník pravoúhlý.\n")

try:
    while True:
        try:
            sides = []
            for i in range(1, 4):
                sides.append(float(input(f"Zadej {i}. stranu: ")))

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
            elif c ** 2 == result:
                print("Trojuhelník je pravoúhlý\n")
            else:
                print("Trojuhelník není pravoúhlý\n")
        except ValueError:
            print("Zadána neplatná hodnota!\n")
except KeyboardInterrupt:
    exit(0)
