numbers = (5, 4, 3, 2)
print(f"1. Výsledek: {sum(numbers)}")

evenNum = 0
oddNum = 0
for n in numbers:
    if n % 2 == 0:
        evenNum += n
    else:
        oddNum += n
print(f"2. Liché: {oddNum}, Sudé: {evenNum}")

print(f"3. Maximální hodnota: {max(numbers)}")

print(f"4. Druhá největší hodnota: {sorted(set(numbers), reverse=True)[1]}")

if list(numbers) == sorted(numbers):
    print("5. Čísla jdou vzestupně")
elif list(numbers) == sorted(numbers, reverse=True):
    print("5. Čísla jdou sestupně")
else:
    print("5. Čísla nejdou vzestupně/sestupně")

for i in range(len(numbers) - 1):
    if (numbers[i] + 1 == numbers[i + 1]) or (numbers[i] - 1 == numbers[i + 1]):
        consecutiveNums = True
    else:
        consecutiveNums = False
        break
if consecutiveNums == True:
    print("6. Čísla jdou po sobě")
else:
    print("6. Čísla nejdou po sobě")

x = 5
if (x in numbers) == True:
    print("7. Číslo se v tuple nachází")
else:
    print("7. Číslo se v tuple nenachází")