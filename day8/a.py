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
answer = 0
for i in range(1,len(lines)-1):
    line = lines[i]
    for j in range(1,len(line)-1):
        tree = int(line[j])
        visible = False
        # check side to side
        if tree > max(rows[i][:j]) or tree > max(rows[i][j+1:]):
            visible = True
        # check up and down
        if tree > max(columns[j][:i]) or tree > max(columns[j][i+1:]):
            visible = True
        if visible: 
            answer += 1
# add edges and subtract corners
answer += len(rows) *2
answer += len(columns) *2
answer -= 4
print(answer)