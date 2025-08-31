import sys

print("Fibonacci sequence v1.0\n")

try:
    while True:
        try:
            n = int(input("Počet čísel fibonacciho posloupnosti: "))
        except ValueError:
            print("""Zadali jste neplatnou hodnotu!
                  Hodnota musí být celé kladné číslo.
                  """)
            continue
        if n <= 0:
            print("""Zadali jste neplatnou hodnotu!
                  Hodnota musí být celé kladné číslo.
                  """)
            continue
        nums = [0, 1]
        if n == 1:
            print(f"Výpis: {nums[0]}\n")
        elif n == 2:  # noqa: PLR2004
            print(f"Výpis: {nums}\n")
        else:
            while n >= len(nums):
                nums.append(nums[-1] + nums[-2])
            print(f"Výpis: {nums}\n")
except KeyboardInterrupt:
    sys.exit(0)
