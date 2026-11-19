str = "the sky is blue"
words = str.split(" ")

reversed_words = [word[::-1] for word in words]

result = " ".join(reversed_words)

print(result)

