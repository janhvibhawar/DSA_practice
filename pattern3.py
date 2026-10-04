n = int(input("Enter number of rows &columns:"))

size = 2 * n - 1
for i in range(size):
    for j in range(size):
        if (i + j == n - 1) or (j - i == n - 1) or (i - j == n - 1) or (i + j == 3 * n - 3):
            print("*", end="")
        else:
            print(" ", end="")
    print()