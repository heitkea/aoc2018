lines = open("data.txt", "r").read().splitlines()

r = 0
freqs = [0]
foundDuplicate = False

def iterateChanges():
    global r, freqs, foundDuplicate
    for s in lines:
        if s[0] == "+":
            r += int(s[1:])
        else:
            r -= int(s[1:])

        if r in freqs:
            print("Found repeat frequency: " + str(r))
            foundDuplicate = True
            break

        freqs.append(r)

while foundDuplicate == False:
    iterateChanges()

# Tries
# -15 wrong
# 245 correct!