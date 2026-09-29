n = int(input("Enter the number of elements: "))

numbers = []
print(f"Enter {n} integers:")
for _ in range(n):
    numbers.append(int(input()))

revnumbers = []
for i in range(n):
    revnumbers.append(numbers[n-i-1])

print(revnumbers)