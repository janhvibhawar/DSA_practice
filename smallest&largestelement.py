n = int(input("Enter the number of elements: "))

numbers = []
print(f"Enter {n} integers:")

for _ in range(n):
    numbers.append(int(input()))

smallest = min(numbers)
largest = max(numbers)

print(f"Smallest element: {smallest}")
print(f"Largest element: {largest}")