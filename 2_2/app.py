lines = open("data.txt", "r").read().splitlines()

def trimID(id, index):
    b = bytearray(id)
    del b[index]
    return str(b)

def parseIDs(id, index):

    for x in range(0, len(id)):
        aID = trimID(id, x)

        for p in range(index+1, len(lines)):
            bID = trimID(lines[p], x)

            if aID == bID:
                print("Found match: " + aID)
                exit

for i in range(0,len(lines)):
    parseIDs(lines[i], i)


# try 1: krdmtuqjgwfoevnaboxglzjph Correct