n = int(input("Enter the number of elements: "))

numbers = []
print(f"Enter {n} integers:")
for _ in range(n):
    numbers.append(int(input()))

count_even = 0
count_odd = 0

for i in range(n):
    if(numbers[i]%2==0):
        count_even+=1
    else:
        count_odd+=1

print("Numbers of even numbers:",count_even)
print("Numbers of odd numbers:", count_odd)