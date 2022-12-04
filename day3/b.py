def priority(i):
    num = ord(i)
    if num > 91:
        # lowercase
        return num - 96
    else:
        # uppercase
        return num - 38

f = open("/Users/meg/Documents/AoC2022/day3/input.txt")
input = f.read().splitlines()

total = 0
x = 0
for x in range(0,len(input),3):
    elf1 = input[x]
    elf2 = input[x+1]
    elf3 = input[x+2]
    for i in elf1:
        if elf2.find(i) > -1 and elf3.find(i) > -1:
            total += priority(i)
            break
print(total)