from math import sqrt

print("2D Distance Calculator v1.0")

try:
    while True:
        try:
            ax = float(input("Zadejte souřadnici x bodu a: "))
            ay = float(input("Zadejte souřadnici y bodu a: "))

            bx = float(input("Zadejte souřadnici x bodu b: "))
            by = float(input("Zadejte souřadnici y bodu b: "))
        except ValueError:
            print("Zadána neplatná hodnota! Opakujte akci znovu.\n")
            continue

        if bx - ax < 0:
            distanceX = ax - bx
        elif bx - ax >= 0:
            distanceX = bx - ax

        if by - ay < 0:
            distanceY = ay - by
        elif by - ay >= 0:
            distanceY = by - ay

        distance = sqrt(distanceX ** 2 + distanceY ** 2)

        print(f"\nVzdálenost bodu a od bodu b je: {distance}\n")
except KeyboardInterrupt:
    exit(0)