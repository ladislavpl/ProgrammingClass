print("Upper-Case Converter v1.0\n")

try:
    while True:
        text = input("Zadejte text: ")
        print(text.upper(), "\n")
except KeyboardInterrupt:
    exit(0)