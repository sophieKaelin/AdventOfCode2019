def pleaseCount(num) :
    temp = int(num / 3) - 2
    if temp <= 0:
        return 0
    return temp + pleaseCount(temp)


file = open('/Users/sophiekaelin/PycharmProjects/AdventOfCode2019/resources/day1input.rtf', 'r')

rawText = file.readlines()
myList = []
counter = 0

for num in rawText:
    temp = num.replace("\\\n","")
    myList.append(temp)
file.close()

myList.pop()

# take its mass, divide by three, round down, and subtract 2.
for num in myList:
    temp = int(num)
    sum = pleaseCount(temp)
    counter = counter + sum

print(counter)
