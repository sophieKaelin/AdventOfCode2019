import math

# CREATING THE LIST
file = open('/Users/sophiekaelin/PycharmProjects/AdventOfCode2019/resources/day5input', 'r')
rawText = file.readlines()

myList = rawText[0].split(',')

for i in range(0, len(myList)):
    myList[i] = int(myList[i])

file.close()
print(myList)

inOut = 5
idx = 0

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

    # Performing Operations dependent on the OPCODE
    if OPCODE == 1:
        myList[myList[idx+3]] = first + second
        idx += 4
    elif OPCODE == 2:
         myList[myList[idx+3]] = first * second
         idx += 4
    elif OPCODE == 3:
        myList[myList[idx+1]] = inOut
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

