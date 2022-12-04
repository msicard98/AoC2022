f = open("/Users/meg/Documents/AoC2022/day4/input.txt")

input = f.read()
lines = input.splitlines()

count = 0
for assignments in lines:
    elfs = assignments.split(",")
    for i in range(len(elfs)):
        elfs[i] = [int(x) for x in elfs[i].split("-")]
    elfs.sort()
    if elfs[0][1] >= elfs[1][0] or elfs[0][0] == elfs[1][0]:
        count += 1
        print(elfs)
print(count)