# read input from text file
f = open("/Users/meg/Documents/AoC2022/day2/input.txt")

# elf
# A = rock 1 point
# B = paper 2 points
# C = scissors  3 points

# you
# X = rock 1 point
# Y = paper 2 points
# Z = scissors 3 points

# +0 for loss
# +3 for draw
# +6 for win

# points for choice
points = {"X":1, "Y":2, "Z":3}
# points for score
score = {
  "A" : {
    "X" : 3,
    "Y" : 6,
    "Z" : 0
  },
  "B" : {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
  },
  "C" : {
    "X" : 6,
    "Y" : 0,
    "Z" : 3
  }
}

total = 0
for line in f:
    # get each players choice
    elf = line[0]
    me = line[2]
    # add points for my choice
    total += points[me]
    # add points for the score
    total += score[elf][me]
# print the score
print(total)
    
