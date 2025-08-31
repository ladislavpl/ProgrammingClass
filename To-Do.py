import sys
from pathlib import Path

print("To-Do v1.1\n")

try:
    while True:
        command = input("Zadej příkaz. Pro nápovědu napiš help: ")
        match command:
            case "help":
                print("""help - Vypíše možné příkazy
                      list - Vypíše všechny úkoly
                      add - Přidá úkol
                      delete - Smaže úkol
                      exit - Ukončí program
                      """)
            case "add":
                with Path.open("list.todo", "a") as f:
                    f.write(f"{input('Zadej úkol: ')}\n")
                print()
            case "delete":
                try:
                    with Path.open("list.todo", "r") as f:
                        lines = f.readlines()
                    linetodelete = int(input("Zadej číslo úkolu: "))
                    if 0 < linetodelete <= len(lines):
                        lines.pop(linetodelete - 1)
                        with Path.open("list.todo", "w") as f:
                            f.writelines(lines)
                        print()
                    else:
                        print("Neplatné číslo úkolu. Zkuste to znovu.\n")
                except FileNotFoundError:
                    print("Soubor nenalezen. Přidejte úkol pomocí příkazu add!\n")
                except ValueError:
                    print("Zadali jste neplatnou hodnotu!\n")
            case "list":
                try:
                    with Path.open("list.todo", "r") as f:
                        lines = f.readlines()
                    if len(lines) == 0:
                        print("To-Do list je prázdný.\n")
                    else:
                        for i in range(1, (len(lines) + 1)):
                            print(f"{i}. {lines[i - 1]}")
                except FileNotFoundError:
                    print("Soubor nenalezen. Přidejte úkol pomocí příkazu add!\n")
            case "exit":
                sys.exit(0)
            case _:
                print("Neplatný příkaz!\n")
except KeyboardInterrupt:
    sys.exit(0)
