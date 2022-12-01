f = open("/Users/meg/Documents/AoC2022/day1/input.txt")

input = f.read()
elfs = input.split("\n\n")

max1 = 0
max2 = 0
max3 = 0
for elf in elfs: 
    calories = elf.split("\n")
    total = sum([eval(i) for i in calories])
    if total > max1: 
        max3 = max2
        max2 = max1
        max1 = total
    elif total > max2 and total < max1:
        max3 = max2
        max2 = total
    elif total > max3 and total < max2:
        max3 = total
print(sum([max1,max2,max3]))