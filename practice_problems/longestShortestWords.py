sentence = "Write a program to accept a sentence"

words = sentence.split()

if words:
    longest = max(words, key=len)
    shortest = min(words, key=len)
    
    print(f"Longest word: {longest}")
    print(f"Shortest word: {shortest}")
else:
    print("The sentence is empty.")
