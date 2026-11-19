main_str = "leetcode"
sub_str = "lee"

count = 0
start = 0

while True:
    pos = main_str.find(sub_str, start)
    if pos == -1:
        break
    count += 1
    start = pos + 1  

print("Occurrences:", count)
