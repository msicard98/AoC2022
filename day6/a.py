f = open("/Users/meg/Documents/AoC2022/day6/input.txt")
input = f.read()

for i in range(len(input)):
    check = [input[i],input[i+1],input[i+2],input[i+3]]
    if len(set(check)) == 4:
        print(i+4)
        break