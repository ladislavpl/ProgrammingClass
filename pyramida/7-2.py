numbers = [1, 2, 3, 4, 10, 15, 34, 32, 96]


for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] += 1

numbers.reverse()

numbers = sorted(numbers)

for n in numbers:
    if n % 5 == 0:
        numbers.pop(numbers.index(n))

print(f"Výsledek: {numbers}")


