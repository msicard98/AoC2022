f = open("/Users/meg/Documents/AoC2022/day4/input.txt")

input = f.read()
lines = input.splitlines()

count = 0
for assignments in lines:
    elfs = assignments.split(",")
    elfs[0] = [int(x) for x in elfs[0].split("-")]
    elfs[1] = [int(x) for x in elfs[1].split("-")]
    elfs.sort()
    if elfs[0][1] >= elfs[1][0] or elfs[0][0] == elfs[1][0]:
        count += 1
print(count)