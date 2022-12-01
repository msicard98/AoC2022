# read input from text file
f = open("/Users/meg/Documents/AoC2022/day1/input.txt")
input = f.read()

# split on different elfs (sections of numbers)
elfs = input.split("\n\n")

max = 0
for elf in elfs: 
    # split on each calorie count for this elf
    calories = elf.split("\n")
    # get total calories for this elf
    total = sum([eval(i) for i in calories])
    # if this elf has the most so far, set to max
    if total > max:
        max = total
# print answer
print(max)