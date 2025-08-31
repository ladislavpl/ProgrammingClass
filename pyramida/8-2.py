import sys  # noqa: INP001

print("Upper-Case Converter v1.0\n")

try:
    while True:
        text = input("Zadejte text: ")
        print(text.upper(), "\n")
except KeyboardInterrupt:
    sys.exit(0)
