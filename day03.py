#https://adventofcode.com/2015/day/3

from AoC import inputData

dataInput = inputData('data/day03.txt')

def main(data):
    #x = up down y = left right
    x = 0
    y = 0
    error = 0
    deliveries = {}
    for i in data:
        if i == ">":
            y = y + 1
        elif i == "<":
            y = y - 1
        elif i == "^":
            x = x + 1
        elif i == "v":
            x = x - 1
        else:
            error = error + 1
        coord = (str(x)+"."+str(y))
        if coord in deliveries:
            deliveries[coord] = deliveries[coord] + 1
        else:
            deliveries[coord] = 1
    if "0.0" in deliveries:
        deliveries["0.0"] = deliveries["0.0"] + 1
    else:
        deliveries["0.0"] = 1
    return (deliveries)

def dataSplit():
    santa = 1
    outputS = ""
    outputRS = ""
    for i in dataInput[0]:
        if santa == 1:
            outputS = outputS + i
            santa = 2
        elif santa == 2:
            outputRS = outputRS + i
            santa = 1
    return outputS, outputRS

def houseCount(houses):
    houseCount = 0
    for a in houses:
        if houses[a] > 0:
            houseCount = houseCount + 1
    return houseCount

def dictNumMerge(dict1, dict2):
    outputDict = {}
    for key in dict1:
        outputDict[key] = dict1[key]
    for key in dict2:
        if key in outputDict:
            outputDict[key] = outputDict[key] + dict2[key]
        else:
            outputDict[key] = dict2[key]
    return outputDict

answer1 = houseCount(main(dataInput[0]))
dataSanta = dataSplit()
answer2S = main(dataSanta[0])
answer2RS = main(dataSanta[1])
outputDict = dictNumMerge(answer2S,answer2RS)
answer2 = houseCount(outputDict)
print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)