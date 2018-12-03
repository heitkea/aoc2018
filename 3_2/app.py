import numpy as np

lines = open("data.txt").read().splitlines()

input = []
fx = 0
fy = 0
fabric = []
overlapCuts = 0

class inputItem:
    def __init__(self, id, x, y, w, h):
        self.id = id
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def hydrateInput():
    global input
    for l in lines:
        larr = l.split(None, 3)
        lcoords = larr[2].split(',',1)
        lwh = larr[3].split('x',1)
        inp = inputItem(larr[0], int(lcoords[0]), int(lcoords[1][:-1]), int(lwh[0]), int(lwh[1]))
        input.append(inp)

def getFabricDimensions():
    global fx, fy, fabric
    for i in input:
        w = i.x + i.w
        if w > fx:
            fx = w
        h = i.y + i.h
        if h > fy:
            fy = h
    fabric = np.zeros( (fx,fy) )

def cutFabric():
    global fabric
    for cut in input: 
        for x in range(cut.x, cut.x + cut.w):
            for y in range(cut.y, cut.y + cut.h):
                fabric[x,y] += 1

def findOverlap():
    global overlapCuts
    for x in range(fx):
        for y in range(fy):
            if fabric[x,y] > 1:
                overlapCuts += 1

def testCuts():
    global fabric
    for cut in input: 
        cutOverlaps = False
        for x in range(cut.x, cut.x + cut.w):
            for y in range(cut.y, cut.y + cut.h):
                if fabric[x,y] > 1:
                    cutOverlaps = True
                    break
            if cutOverlaps == True:
                break
        if cutOverlaps == False:
            return cut.id

hydrateInput()
getFabricDimensions()
cutFabric()
findOverlap()
print("\r\nNo overlap: " + testCuts() + "\r\n")

# try 1: 909 correct!