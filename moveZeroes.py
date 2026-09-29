n = int(input("Enter the number of elements: "))

numbers = []
print(f"Enter {n} integers:")
for _ in range(n):
    numbers.append(int(input()))

new_array = []
count = 0

for i in range (n):
    if(numbers[i]!=0):
        new_array.append(numbers[i])
    else:
        count+=1

for i in range (count):
    new_array.append(0)

print(new_array)