class Directory:
    def __init__(self, parent):
        self.data = 0
        self.parent = parent
    def adddata(self, data):
        self.data += data
    def getdata(self):
        return self.data
    def getparent(self):
        return self.parent

f = open("/Users/meg/Documents/AoC2022/day7/input.txt")

# create file tree
nodes = []
root = Directory(None)
nodes.append(root)
currentdir = root
previous = None
for line in f:
    if line[0:7] == "$ cd ..":
        # change directory
        currentdir = currentdir.getparent()
    elif line[0:3] == "$ c":
        # change directory
        previous = currentdir
        currentdir = Directory(previous)
        nodes.append(currentdir)
    elif line[0].isdigit():
        # size of file
        currentdir.adddata(int(line.split()[0]))

# run totals 
nodes.reverse()
for node in nodes:
    data = node.getdata()
    if node.getparent() is not None:
        node.getparent().adddata(data)

# get small files total
total = 0
for node in nodes: 
    if node.getdata() <= 100000:
        total += node.getdata()

print(total)