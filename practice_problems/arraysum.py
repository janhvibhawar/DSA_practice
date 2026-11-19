n = int(input("Enter the number of elements: "))

numbers = []
print(f"Enter {n} integers:")
for _ in range(n):
    numbers.append(int(input()))

sum = 0

for num in numbers:
    sum += num

print("The sum using loop is:", sum)

