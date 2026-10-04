n = int(input("Enter number of rows:"))
mid = n//2

for i in range (n):
    for j in range (n):
        if i == mid or j == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
 