import numpy as numpy

lines = open("data.txt").read().splitlines()

preinput = []
input = []
fx = 0
fy = 0
schedule = numpy.zeros((2,62))
sleep = {"id":0}
sleepByGuard = { 0 : 0 }

class inputItem:
    def __init__(self, id, gdate, gtime, stime,action):
        self.id = id
        self.gdate = gdate
        self.gtime = gtime
        self.stime = stime
        self.action = action
        self.sortDate = str(gdate) + " " + str(gtime)
    def __str__(self):
        return "id:" + str(self.id) + " date:" + str(self.gdate) + " time:" + str(self.gtime) + " action:" + str(self.action) + " sort:" + str(self.sortDate)
        
def sortInput():
    global preinput
    for l in lines:
        datePart = l.split("]",1)[0][1:]
        preinput.append([datePart, l])
    preinput.sort(key=lambda x: x[0], reverse=False)
    #print(preinput)

def hydrateInput():
    global input
    currentGuardId = ""
    for l in preinput:
        larr = l[1].split(None, 2)
        gdate = larr[0].split("-",1)[1]
        stime = larr[1].split(":",1)
        stime = stime[1][:-1]
        gtime = stime
        if gtime[0] == "0":
            gtime = gtime[1]
        arraction = larr[2]
        saction = arraction.split(None,1)
        if saction[0] == "Guard":
            id = saction[1].split(None,1)[0]
            currentGuardId = id
            action = "wake"
        else:
            id = currentGuardId
            if saction[1] == "up":
                action = "wake"
            else:
                action = "sleep"

        inp = inputItem(id, gdate, gtime, stime,action)
        input.append(inp)
        print(inp)
        
def hydrateSchedule():
    isAsleep = False
    currentId = ""
    start = ""
    stop = ""
    global sleep
    for i in input:
        if (str(i.id)+str(i.gdate)) != currentId:
            currentId = str(i.id)+str(i.gdate)
            start = ""

        if i.action == "sleep":
            isAsleep = True
            start = i.gtime
        else:
            isAsleep = False
            stop = i.gtime

        if isAsleep == False and start != "": # create entry
            if i.id in sleep:
                sleep[i.id] += int(stop)-int(start)
            else:
                sleep[i.id] = int(stop) - int(start)

    sortedSleep = sorted(sleep.items(), key=lambda sleep: sleep[1], reverse=True)
    print(sortedSleep)
    return sortedSleep[0]

def getFreqHours(guardid):
    isAsleep = False
    currentId = ""
    start = ""
    stop = ""
    global sleep, sleepByGuard
    for i in input:
        if (str(i.id)+str(i.gdate)) != currentId:
            currentId = str(i.id)+str(i.gdate)
            start = ""

        if i.action == "sleep":
            isAsleep = True
            start = i.gtime
        else:
            isAsleep = False
            stop = i.gtime

        if isAsleep == False and start != "" and i.id == guardid: # create entry
            for i in range(int(start),int(stop)):
                if i in sleepByGuard:
                    sleepByGuard[i] += 1
                else:
                    sleepByGuard[i] = 1

    sleepByGuard = sorted(sleepByGuard.items(), key=lambda sleepByGuard: sleepByGuard[1], reverse=True)
    print(sleepByGuard)

sortInput()
hydrateInput()
guardid = hydrateSchedule()
print(guardid)
getFreqHours(guardid[0])

# try 1: 125444 correct!
