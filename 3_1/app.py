lines = open("data.txt").read().splitlines()

tries = 0

def trimID(id, index):
    b = bytearray(id)
    del b[index]
    return str(b)

def parseIDs(id, index):

    for x in range(0, len(id)):
        aID = trimID(id, x)

        for p in range(index+1, len(lines)):
            bID = trimID(lines[p], x)

            global tries
            tries += 1

            if aID == bID:
                print("\r\nFound match: " + aID + " Index: " + str(index) + " of " + str(len(lines)) + " Tries: " + str(tries) + "\r\n")
                exit

for i in range(0,len(lines)):
    parseIDs(lines[i], i)

# try 1: krdmtuqjgwfoevnaboxglzjph Correct