import sys  # noqa: INP001

print("Character Counter v1.0\n")

try:
    while True:
        text = input("Zadejte text: ")
        print(f"Délka textu je: {len(text)}\n")
except KeyboardInterrupt:
    sys.exit(0)
