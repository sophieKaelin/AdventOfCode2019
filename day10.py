file = open('/Users/sophiekaelin/PycharmProjects/AdventOfCode2019/resources/day10input', 'r')
rawText = file.readlines()

myList = []
for item in rawText:
    myList.append(item.strip('\n'))
print(myList)

