n = int(input("Enter the number of elements: "))

numbers = []
print(f"Enter {n} integers:")
for _ in range(n):
    numbers.append(int(input()))

searching_number = int(input("Enter number to search:"))

flag = 0
for i in range (n):
    if(numbers[i]==searching_number):
        flag = 1
        break

if(flag==1):
    print("Yes the number is present in array at position : ", i)
else:
    print("No the number is not present in array")

