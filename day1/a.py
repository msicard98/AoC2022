f = open("/Users/meg/Documents/AoC2022/day1/input.txt")

input = f.read()
elfs = input.split("\n\n")

max = 0
for elf in elfs: 
    calories = elf.split("\n")
    total = sum([eval(i) for i in calories])
    if total > max:
        max = total
print(max)