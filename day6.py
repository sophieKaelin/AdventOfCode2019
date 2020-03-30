# CREATING THE LIST
file = open('/Users/sophiekaelin/PycharmProjects/AdventOfCode2019/resources/day6input', 'r')
rawText = file.readlines()

myList = []
basePlanet = "QWS"

for i in range(0, len(rawText)):
    myList.append(rawText[i][:-1])

file.close()
print(myList)

def createYouList(planet):
    if planet[0] == basePlanet:
        return
    for item in fullList:
        if item[0] == planet[1]:
            youList.append(item)
            createYouList(item)
    return

def createSanList(planet):
    if planet[0] == basePlanet:
        return
    for item in fullList:
        if item[0] == planet[1]:
            sanList.append(item)
            createSanList(item)
    return


# How many planets the given planet orbits
def countOrbits(planet):
    if planet == basePlanet:
        return 0
    for item in myList:
        if item[-3:] == planet:
            return 1 + countOrbits(item[:3])
    return 0

# Set first values.
# myList[0][:3] is First code (previous)
# myList[0][-3:] is Last code (current)

# [planet orbits, this planet]
# fullList = [myList[0][-3:], myList[0][:3], countOrbits(myList[0][-3:])]
fullList = []

# find how many planets orbit each other planet.

for item in myList:
    fullList.append([item[-3:], item[:3], 1 + countOrbits(item[:3])])

# Once List created, parse through with a counter to count number of orbits and indirect orbits.
counter = 0

for item in fullList:
    counter += item[2]

print("Number of Orbits: ", counter)

# Create YOU path and SAN path
youList = []
sanList = []

# Start the list
for item in fullList:
    if item[0] == "YOU":
        youList.append(item)
        print("BAM", youList)
    if item[0] == "SAN":
        sanList.append(item)

# YOU LOOP
createYouList(youList[0])
createSanList(sanList[0])
print("youlist", youList)
print("sanlist", sanList)

# FIND COMMON PLANETS
commonList = []
for yous in youList:
    for sans in sanList:
        if sans[0] == yous[0]:
            commonList.append(yous)
print("commonlist", commonList)

# FIND MIN DISTANCE FOR EACH COMMON
minDistance = 99999999999999999999999999999999999999999999999999999999999999999
for planet in commonList:
    dist = youList[0][2] + sanList[0][2] - (2 * planet[2]) - 2
    minDistance = min(minDistance, dist)
print("min Distance", minDistance)



