print("Malá násobilka dvou\n")  # noqa: INP001

for i in range(1, 11):
    if i == 10:  # noqa: PLR2004
        print(i * 2)
    else:
        print(i * 2, end=", ")
