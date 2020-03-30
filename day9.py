import math

# CREATING THE LIST
file = open('/Users/sophiekaelin/PycharmProjects/AdventOfCode2019/resources/day9input', 'r')
rawText = file.readlines()

myList = rawText[0].split(',')

for i in range(0, len(myList)):
    myList[i] = int(myList[i])

file.close()

for i in range(0, len(myList)):
    myList.append(0)
print(myList)

inOut = 2
idx = 0
relBase = 0

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
        elif abs(math.floor(myList[idx] /100)) % 10 == 2:
            first = myList[myList[idx+1] + relBase]
        else:
            first = myList[idx+1]
        if OPCODE != 4 and OPCODE != 9: # OPCODE 4 and 9 doesn't have a second parameter.
            #     if the length < 4 then has to be type 0, or check the thousands column
            if length < 4 or abs(math.floor(myList[idx] /1000)) % 10 == 0:
                second = myList[myList[idx+2]]
            elif abs(math.floor(myList[idx] /1000)) % 10 == 2:
                second = myList[myList[idx+2] + relBase]
            else:
                second = myList[idx+2]
    #         THIRD PARAM NOW
    if OPCODE == 1 or OPCODE == 2 or OPCODE == 7 or OPCODE == 8:
        if abs(math.floor(myList[idx] /10000)) % 10 == 2:
            third = myList[idx+3] + relBase
        else:
            third = myList[idx+3]

    # Performing Operations dependent on the OPCODE
    if OPCODE == 1:
        myList[third] = first + second
        idx += 4
    elif OPCODE == 2:
         myList[third] = first * second
         idx += 4
    elif OPCODE == 3:
        if abs(math.floor(myList[idx] /100)) % 10 == 0:
            myList[myList[idx+1]] = inOut
        else:
            myList[myList[idx+1] + relBase] = inOut
        idx += 2
    elif OPCODE == 4:
        inOut = first
        print("Output:", inOut)
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
            myList[third] = 1
        else:
            myList[third] = 0
        idx += 4
    elif OPCODE == 8:
        if first == second:
            myList[third] = 1
        else:
            myList[third] = 0
        idx += 4
    elif OPCODE == 9:
        relBase += first
        idx += 2
    else:
        print("halt")

print(inOut)
