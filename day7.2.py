import itertools, math
# CREATING THE LIST

def doTheThing(phaseInstr, prevOut, isFirst, phaseNum):
    global outputed
    file = open('/Users/sophiekaelin/PycharmProjects/AdventOfCode2019/resources/day7input', 'r')
    rawText = file.readlines()

    myList = rawText[0].split(',')
    myList[len(myList) -1 ] = 99

    for i in range(0, len(myList)):
        myList[i] = int(myList[i])

    file.close()
    idx = 0
    inOut = prevOut
    used = True

    # Looping through values until 99 is found.
    while myList[idx] != 99:
        length = len(str(myList[idx]))

        # Determine the OPCODE
        if length == 1:
            OPCODE = abs(myList[idx])
        else :
            OPCODE = abs(myList[idx]) % 10


        # Parameter type checks
        if OPCODE != 3: #OPCODE 3 Will always using parameter mode 0
            #     Determine 1st Param if the value only contains an OPCODE OR if the value in hundreds column is 0
            if length == 1 or length == 2 or abs(math.floor(myList[idx] /100)) % 10 == 0:
                first = myList[myList[idx+1]]
            else:
                first = myList[idx+1]
            if OPCODE != 4: # OPCODE 4 doesn't have a second parameter.
                #     if the length < 4 then has to be type 0, or check the thousands column
                if length != 4 or abs(math.floor(myList[idx] /1000)) % 10 == 0:
                    second = myList[myList[idx+2]]
                else:
                    second = myList[idx+2]

        print(OPCODE)
        # Performing Operations dependent on the OPCODE
        if OPCODE == 1:
            myList[myList[idx+3]] = first + second
            idx += 4
        elif OPCODE == 2:
             myList[myList[idx+3]] = first * second
             idx += 4
        elif OPCODE == 3:
            if isFirst:
                myList[myList[idx+1]] = phaseInstr
                isFirst = False
                inOut = prevOut
            else:
                myList[myList[idx+1]] = inOut
            idx += 2
            if used:
                used = False
            else:
                idxs[phaseNum] = idx
                return inOut
        elif OPCODE == 4:
            outputed = True
            inOut = first
            # print("Output:", inOut)
            return inOut
            idx += 2
        elif OPCODE == 5:
            if first != 0:
                idx = second
            else:
                idx += 3
        elif OPCODE == 6:
            if first == 0:
                idx = second
            else:
                idx += 3
        elif OPCODE == 7:
            if first < second:
                myList[myList[idx+3]] = 1
            else:
                myList[myList[idx+3]] = 0
            idx += 4
        elif OPCODE == 8:
            if first == second:
                myList[myList[idx+3]] = 1
            else:
                myList[myList[idx+3]] = 0
            idx += 4
        else:
            print("halt")
    return inOut

# data = list(itertools.permutations([0, 1, 2, 3, 4], 5))
#
# maxVal = 0
# for item in data:
#     outp = 0
#     for i in item:
#         print(i)
#         outp = doTheThing(i, outp)
#     maxVal = max(maxVal, outp)
#
# print("largest ", maxVal)

# Part 2

outputed = False
data = list(itertools.permutations([5, 6, 7, 8, 9], 5))
idxs = [0, 0, 0, 0, 0]
maxVal = 0
for item in data:
    print(item)
    outp = 0
    outputed = False
    # FIRST TIME INPUT AS NORMAL
    for i in range(0, 5):
        outp = doTheThing(item[i], outp, True, i)
    # SECOND TIME REPEAT - FIND WAY TO LOOP
    while outputed == False:
        for i in range(0, 5):
            outp = doTheThing(item[i], outp, False, i)

    maxVal = max(maxVal, outp)

print("largest ", maxVal)

