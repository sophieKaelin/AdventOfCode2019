# Remove all consequetive numbers
def continueRem(item, dig):
    stri = str(item)
    if len(stri) == 0:
        return 0
    if len(stri) == 1:
        if int(stri) == dig:
            return 0
        else:
            return item
    if(int(stri[0]) == dig):
        return continueRem(int(stri[1:]), dig)
    else:
        return item

def adjacent(item):
    stri = str(item)
    if stri == '0':
        return False
    if len(stri) == 1:
        return False
    if len(stri) == 2:
        if(int(stri[0]) == int(stri[1])):
            return True
    if(int(stri[0]) == int(stri[1])):
        # PART 2
        if(int(stri[2]) == int(stri[1])):
            # Remove all repeated digits
            return adjacent(continueRem(int(stri), int(stri[0])))
        else:
            return True
    return adjacent(int(stri[1:]))


def ascend(item):
    stri = str(item)
    if stri == '0':
        return True
    if len(stri) == 1:
        return True
    if len(stri) == 2:
        if(int(stri[0]) <= int(stri[1])):
            return True
    if(int(stri[0]) <= int(stri[1])):
        return ascend(int(stri[1:]))
    return False

# Range: 138241-674034
count = 0
for i in range(138241, 674034):
    if ascend(i) and adjacent(i):
        count+=1

print(count)

