print("Fibonacci sequence v1.0\n")

try:
    while True:
        try:
            n = int(input("Počet čísel fibonacciho posloupnosti: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\nHodnota musí být celé kladné číslo.\n")
            continue
        if n <= 0:
            print("Zadali jste neplatnou hodnotu!\nHodnota musí být celé kladné číslo.\n")
            continue
        nums = [0, 1]
        if n == 1:
            print(f"Výpis: {nums[0]}\n")
        elif n == 2:
            print(f"Výpis: {nums}\n")
        else:
            while n >= len(nums):
                nums.append(nums[-1] + nums[-2])
            print(f"Výpis: {nums}\n")
except KeyboardInterrupt:
    exit(0)
