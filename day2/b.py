# read input from text file
f = open("/Users/meg/Documents/AoC2022/day2/input.txt")

# points for choice
score = {"X":0, "Y":3, "Z":6}
# points for score
me = {
  "A" : {
    "X" : 3,
    "Y" : 1,
    "Z" : 2
  },
  "B" : {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
  },
  "C" : {
    "X" : 2,
    "Y" : 3,
    "Z" : 1
  }
}

total = 0
for line in f:
    # get each players choice
    elf = line[0]
    end = line[2]
    # add points for the score
    total += score[end]
    # add points for my choice
    total += me[elf][end]
# print the score
print(total)
    
