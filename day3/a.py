def priority(i):
    num = ord(i)
    if num > 91:
        # lowercase
        return num - 96
    else:
        # uppercase
        return num - 38

f = open("/Users/meg/Documents/AoC2022/day3/input.txt")

total = 0
for line in f:
    half = int(len(line)/2)
    front = line[:half]
    back = line[half:]
    for i in front:
        if back.find(i) > -1:
            total += priority(i)
            break
print(total)

