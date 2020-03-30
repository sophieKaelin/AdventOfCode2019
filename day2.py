import copy
file = open('/Users/sophiekaelin/PycharmProjects/AdventOfCode2019/resources/day2input', 'r')
idx = 0
noun = 0
verb = 0
rawText = file.readlines()
temp = 0

myList = rawText[0].split(',')
myList[len(myList) -1 ] = 0

for i in range(0, len(myList)):
    myList[i] = int(myList[i])

file.close()

OGCopy = copy.deepcopy(myList)
myList[1] = 0
myList[2] = myList[2] + 1

while verb <= 99:
    noun = 0
    while noun <= 99:
        idx = 0
        while myList[idx] != 99:
            first = myList[myList[idx+1]]
            second = myList[myList[idx+2]]

            if myList[idx] == 1:
                myList[myList[idx+3]] = first + second
            elif myList[idx] == 2:
                 myList[myList[idx+3]] = first * second
            else:
                print("halt")
            idx = idx + 4

        # CHECK
        if(myList[0]) == 19690720:
            print(myList[1])
            print(myList[2])
            print(100 * myList[1] + myList[2])
            print("FOUND IT")

        noun+=1
        myList = copy.deepcopy(OGCopy)
        myList[1] = noun
        myList[2] = verb
    verb +=1
    myList[2] = verb

print(myList[0])

