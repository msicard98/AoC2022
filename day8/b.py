def left(tree, check):
    count = 0
    check.reverse()
    for other in check:
        count += 1
        if other >= tree:
            break
    return count
def right(tree, check):
    count = 0
    for other in check:
        count += 1
        if other >= tree:
            break
    return count
def up(tree, check):
    count = 0
    check.reverse()
    for other in check:
        count += 1
        if other >= tree:
            break
    return count
def down(tree, check):
    count = 0
    for other in check:
        count += 1
        if other >= tree:
            break
    return count

f = open("/Users/meg/Documents/AoC2022/day8/input.txt")
lines = f.read().split("\n")
# make lists for rows and columns
rows = []
columns = []
for i in range(len(lines[0])):
    columns.append([])
for line in lines:
    rows.append([int(i) for i in line])
    count = 0
    for x in line:
        columns[count].append(int(x))
        count += 1
# check visibility 
answers = []
for i in range(1,len(lines)-1):
    line = lines[i]
    for j in range(1,len(line)-1):
        tree = int(line[j])
        # check side to side
        leftcount = left(tree, rows[i][:j])
        rightcount = right(tree, rows[i][j+1:])
        upcount = up(tree, columns[j][:i])
        downcount = down(tree, columns[j][i+1:])
        answers.append(leftcount * rightcount * upcount * downcount)
# add edges and subtract corners

print(max(answers))