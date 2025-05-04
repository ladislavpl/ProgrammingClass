print("Horses and People v1.0\n")

for i in range(23):
    horses = 22 - i
    legs = 2 * i + 4 * horses
    if legs == 72:
        print(f"Nalezen výsledek!\nKoně: {horses}\nLidé: {i}\n")
        break