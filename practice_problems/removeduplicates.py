n = int(input("Enter the number of elements: "))

numbers = []
print(f"Enter {n} integers:")
for _ in range(n):
    numbers.append(int(input()))

new_array = []

for i in range (n):
    if numbers[i] in new_array:
        continue
    else:
        new_array.append(numbers[i])

print(new_array)