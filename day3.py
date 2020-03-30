
file = open('/Users/sophiekaelin/PycharmProjects/AdventOfCode2019/resources/day3input', 'r')
rawText = file.readlines()
file.close()

myList1 = rawText[0].split(',')
myList2 = rawText[1].split(',')
myList1[len(myList1) -1 ] = "R294"
myList2[len(myList1) -1 ] = "R672"
print(myList1)
print(myList2)

coord1 = [[0, 0]]
coord2 = [[0, 0]]

cross = [[0, 0]]
shortestTotal = 99999999999999999999999999999999999999999999999999999999999
#part 2
def calculateDistance(coo1, thelist):
    if coo1 == 0:
        return 0
    return int(thelist[coo1-1][1:]) + calculateDistance(coo1-1, thelist)

x = 0
y = 0
## Store points in 2D list
for item in myList1:
    val = int(item[1:])
    if 'R' in item:
        x = x + val
    elif 'L' in item:
        x = x - val
    elif 'D' in item:
        y = y - val
    else:
        y = y + val
    coord1.append([x, y])
print(coord1)

x = 0
y = 0
for item in myList2:
    val = int(item[1:])
    if 'R' in item:
        x = x + val
    elif 'L' in item:
        x = x - val
    elif 'D' in item:
        y = y - val
    else:
        y = y + val
    coord2.append([x, y])
print(coord2)

count = 0
for cord1 in range(len(coord1)-2, 0, -1):
    print(cord1)
    for cord2 in range(len(coord2)-2, 0, -1):
            # if x and y
            if(coord1[cord1+1][0] == coord1[cord1][0] and coord2[cord2+1][1] == coord2[cord2][1]):
                # if in the range of y
                large = max(coord1[cord1+1][1],coord1[cord1][1])
                small = min(coord1[cord1+1][1],coord1[cord1][1])
                if(small < coord2[cord2][1] < large):
                    large = max(coord2[cord2+1][0],coord2[cord2][0])
                    small = min(coord2[cord2+1][0],coord2[cord2][0])
                    if(small < coord1[cord1][0] < large):
                        cross.append([coord1[cord1][0], coord2[cord2][1]])
                        if (calculateDistance(cord2, myList2) + calculateDistance(cord1, myList1)) < shortestTotal:
                            shortestTotal = calculateDistance(cord2, myList2) + calculateDistance(cord1, myList1) + abs(coord2[cord2][1] - coord1[cord1][1]) + abs(coord1[cord1][0] - coord2[cord2][0])
            # if y and x
            if(coord1[cord1+1][1] == coord1[cord1][1] and coord2[cord2+1][0] == coord2[cord2][0]):
                # if in the range of x
                large = max(coord1[cord1+1][0],coord1[cord1][0])
                small = min(coord1[cord1+1][0],coord1[cord1][0])
                if(small < coord2[cord2][0] < large):
                    large = max(coord2[cord2+1][1],coord2[cord2][1])
                    small = min(coord2[cord2+1][1],coord2[cord2][1])
                    if(small < coord1[cord1][1] < large):
                        cross.append([coord1[cord1][1], coord2[cord2][0]])
                        if (calculateDistance(cord2, myList2) + calculateDistance(cord1, myList1)) < shortestTotal:
                            shortestTotal = calculateDistance(cord2, myList2) + calculateDistance(cord1, myList1) + abs(coord2[cord2][1] - coord1[cord1][1]) + abs(coord1[cord1][0] - coord2[cord2][0])

## Find Distance of each cross
# shortest = abs(cross[1][0]) + abs(cross[1][1])
# for i in range(2, len(cross)):
#     shortest = min(shortest, abs(cross[i][0]) + abs(cross[i][1]))

print(shortestTotal)


