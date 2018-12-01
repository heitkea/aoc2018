lines = open("data.txt", "r").read().splitlines()

r = 0
freqs = [0]
foundDuplicate = False

def iterateChanges(r):
    foundDuplicate = False
    for s in lines:
        if s[0] == "+":
            r += int(s[1:])
        else:
            r -= int(s[1:])

        if r in freqs:
            print "Found repeat frequency: " + str(r)
            foundDuplicate = True
            break

        freqs.append(r)

    return [r, foundDuplicate]

while foundDuplicate == False:
    print len(freqs)
    res = iterateChanges(r)
    r = res[0]
    foundDuplicate = res[1]
    
# Tries
# -15 wrong
# 245 correct!