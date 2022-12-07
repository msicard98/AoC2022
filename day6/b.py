f = open("/Users/meg/Documents/AoC2022/day6/input.txt")
input = f.read()

for i in range(len(input)):
    check = [x for x in input[i:i+14]]
    if len(set(check)) == 14:
        print(i+14)
        break