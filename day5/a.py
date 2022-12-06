f = open("/Users/meg/Documents/AoC2022/day5/input.txt")

# create stacks 
stacks = [
    ["S","L","W"],
    ["J","T","N","Q"],
    ["S","C","H","F","J"],
    ["T","R","M","W","N","G","B"],
    ["T","R","L","S","D","H","Q","B"],
    ["M","J","B","V","F","H","R","L"],
    ["D","W","R","N","J","M"],
    ["B","Z","T","F","H","N","D","J"],
    ["H","L","Q","N","B","F","T"]
]

# move crates
for line in f:
    moves = [int(i) for i in line.split() if i.isdigit()]
    for i in range(moves[0]):
        crate = stacks[moves[1]-1].pop()
        stacks[moves[2]-1].append(crate)

# print answer 
for stack in stacks: 
    print(stack.pop())