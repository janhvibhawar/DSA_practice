def anagram(n1: int, n2: int) -> bool:
    return sorted(str(int(n1))) == sorted(str(int(n1)))

def main():
    num1 = 1221
    num2 = 1212
    
    result = anagram(num1, num2)
    print(f"Are {num1} and {num2} anagrams? {result}")

if __name__ == "__main__":
    main()
