import matplotlib.pyplot as plt
import numpy as np

file = open('/Users/sophiekaelin/PycharmProjects/AdventOfCode2019/resources/day8input', 'r')
rawText = file.readlines()

myList = rawText[0].split('\n')
file.close()

str = myList[0]
o = []
while str:
    o.append(str[:150])
    str = str[150:]
print(o)

# Find layer with fewest 0 digits
lowestVal = 999999999999999999999999999999
greatestIdx = 0
for idx in range (0, len(o)):
    numZero = o[idx].count("0")
    if(numZero < lowestVal):
        lowestVal = numZero
        greatestIdx = idx

print(o)

numOnes = o[greatestIdx].count("1")
numTwos = o[greatestIdx].count("2")
answer = numOnes * numTwos
print("Answers = ", answer)

# PART 2
lastList = []
for i in range(0, 150):
    idxx = 0
    while idxx < 100 and o[idxx][i] == '2':
        idxx +=1
    print(int(o[idxx][i]))
    lastList.append(int(o[idxx][i]))


print(len(lastList))
print(lastList)


# plt.imshow(lastList, cmap="gray")
# plt.show()

