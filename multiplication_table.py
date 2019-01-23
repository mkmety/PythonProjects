size = int(input("Choose the size of the multiplication table (up to 20): "))
dash = "-" * (size * 4)
if size <= 20:
    print(dash)
    print(*range(1, (size + 1)), sep="\t")
    print(dash)
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print(i * j, end="\t")
        print("")
else:
    print("Size of multiplication table not supported")
