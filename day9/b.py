# here's what I am doing wrong
# direction of head does not correlate to direction tails 
# tails can move diagonally unlike heads so original functions don't work
## comparing head to tail is not same and tail to tail
def movetailr(hx,hy,tx,ty):
    if hy == ty and hx-tx == 2:
        #print("move right")
        return [tx+1,ty]
    elif hy != ty and hx-tx == 2:
        #print("move diagonal")
        return [hx-1,hy]
    else:
        #print("don't move")
        return [tx,ty]
def movetaill(hx,hy,tx,ty):
    if hy == ty and tx-hx == 2:
        #print("move left")
        return [tx-1,ty]
    elif hy != ty and tx-hx == 2:
        #print("move diagonal")
        return [hx+1,hy]
    else:
        #print("don't move")
        return [tx,ty]
def movetailu(hx,hy,tx,ty):
    if hx == tx and hy-ty == 2:
        #print("move up")
        return [tx,ty+1]
    elif hx != tx and hy-ty == 2:
        #print("move diagonal")
        return [hx,hy-1]
    else:
        #print("don't move")
        return [tx,ty]
def movetaild(hx,hy,tx,ty):
    if hx == tx and ty-hy == 2:
        #print("move down")
        return [tx,ty-1]
    elif hx != tx and ty-hy == 2:
        #print("move diagonal")
        return [hx,hy+1]
    else:
        #print("don't move")
        return [tx,ty]

f = open("/Users/meg/Documents/AoC2022/day9/input.txt")

visits = []
hx = 0
hy = 0
tailx = [0,0,0,0,0,0,0,0,0]
taily = [0,0,0,0,0,0,0,0,0]
for line in f:
    dir = line.split()[0]
    num = int(line.split()[1])
    # move head
    #print(dir)
    if dir == "R":
        for i in range(num):
            hx += 1
            tail = movetailr(hx,hy,tailx[0],taily[0])
            tailx[0] = tail[0]
            taily[0] = tail[1]
            for j in range(1,9):
                tail = movetailr(tailx[j-1],taily[j-1],tailx[j],taily[j])
                tailx[j] = tail[0]
                taily[j] = tail[1]
            visits.append("{}-{}".format(tailx[8],taily[8]))
    elif dir == "L":
        for i in range(num):
            hx -= 1
            tail = movetaill(hx,hy,tailx[0],taily[0])
            tailx[0] = tail[0]
            taily[0] = tail[1]
            for j in range(1,9):
                tail = movetaill(tailx[j-1],taily[j-1],tailx[j],taily[j])
                tailx[j] = tail[0]
                taily[j] = tail[1]
            visits.append("{}-{}".format(tailx[8],taily[8]))
    elif dir == "U":
        for i in range(num):
            hy += 1
            tail = movetailu(hx,hy,tailx[0],taily[0])
            tailx[0] = tail[0]
            taily[0] = tail[1]
            for j in range(1,9):
                tail = movetailu(tailx[j-1],taily[j-1],tailx[j],taily[j])
                tailx[j] = tail[0]
                taily[j] = tail[1]
            visits.append("{}-{}".format(tailx[8],taily[8]))
    elif dir == "D":
        for i in range(num):
            hy -= 1
            tail = movetaild(hx,hy,tailx[0],taily[0])
            tailx[0] = tail[0]
            taily[0] = tail[1]
            for j in range(1,9):
                tail = movetaild(tailx[j-1],taily[j-1],tailx[j],taily[j])
                tailx[j] = tail[0]
                taily[j] = tail[1]
            visits.append("{}-{}".format(tailx[8],taily[8]))
print(len(set(visits)))