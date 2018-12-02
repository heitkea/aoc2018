lines = open("data.txt", "r").read().splitlines()

threes = 0
twos = 0

def parseIDs(id):

    charList = [["a",0]]

    # sum characters
    for i in id:
        found = False
        for x in charList:
            if x[0] == i:
                x[1] += 1
                found = True
                break
        
        if found == False:
            charList.append([i,1])

    threeChars = list(filter(lambda x: x[1] == 3, charList))
    global threes
    if (len(threeChars) > 0):
        threes += 1

    twoChars = list(filter(lambda x: x[1] == 2, charList))
    global twos
    if (len(twoChars) > 0):
        twos += 1

for l in lines:
    parseIDs(l)

print(threes * twos)

# try 1: 5952 Correct