# read input from text fileS
f = open("/Users/meg/Documents/AoC2022/day1/input.txt")
input = f.read()

# split on different elfs (sections of numbers)
elfs = input.split("\n\n")

# keep track of the top 3 totals
max1 = 0
max2 = 0
max3 = 0
for elf in elfs: 
    # split on each calorie count for this elf
    calories = elf.split("\n")
    # get total calories for this elf
    total = sum([eval(i) for i in calories])
    # if this elf has more than any of the top 3, set and demote others
    if total > max1: 
        max3 = max2
        max2 = max1
        max1 = total
    elif total > max2 and total < max1:
        max3 = max2
        max2 = total
    elif total > max3 and total < max2:
        max3 = total
# print answer
print(sum([max1,max2,max3]))