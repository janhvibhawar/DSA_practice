s = input("Enter a string:")

vowels = "aeiouAEIOU"
v_count = c_count = d_count = s_count = 0
    
for char in s:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1
    elif char.isdigit():
            d_count += 1
    else:
            s_count += 1
            
print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")
print(f"Digits: {d_count}")
print(f"Special Characters: {s_count}")