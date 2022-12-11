def movetailr(hx,hy,tx,ty):
    if hy == ty and hx-tx == 2:
        return [tx+1,ty]
    elif hy != ty and hx-tx == 2:
        return [hx-1,hy]
    else:
        return [tx,ty]
def movetaill(hx,hy,tx,ty):
    if hy == ty and tx-hx == 2:
        return [tx-1,ty]
    elif hy != ty and tx-hx == 2:
        return [hx+1,hy]
    else:
        return [tx,ty]
def movetailu(hx,hy,tx,ty):
    if hx == tx and hy-ty == 2:
        return [tx,ty+1]
    elif hx != tx and hy-ty == 2:
        return [hx,hy-1]
    else:
        return [tx,ty]
def movetaild(hx,hy,tx,ty):
    if hx == tx and ty-hy == 2:
        return [tx,ty-1]
    elif hx != tx and ty-hy == 2:
        return [hx,hy+1]
    else:
        return [tx,ty]

f = open("/Users/meg/Documents/AoC2022/day9/input.txt")

visits = []
hx = 0
hy = 0
tx = 0
ty = 0
for line in f:
    dir = line.split()[0]
    num = int(line.split()[1])
    # move head
    if dir == "R":
        for i in range(num):
            hx += 1
            tail = movetailr(hx,hy,tx,ty)
            tx = tail[0]
            ty = tail[1]
            visits.append("{}-{}".format(tx,ty))
    elif dir == "L":
        for i in range(num):
            hx -= 1
            tail = movetaill(hx,hy,tx,ty)
            tx = tail[0]
            ty = tail[1]
            visits.append("{}-{}".format(tx,ty))
    elif dir == "U":
        for i in range(num):
            hy += 1
            tail = movetailu(hx,hy,tx,ty)
            tx = tail[0]
            ty = tail[1]
            visits.append("{}-{}".format(tx,ty))
    elif dir == "D":
        for i in range(num):
            hy -= 1
            tail = movetaild(hx,hy,tx,ty)
            tx = tail[0]
            ty = tail[1]
            visits.append("{}-{}".format(tx,ty))
print(len(set(visits)))

    

