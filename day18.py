#https://adventofcode.com/2015/day/18

from AoC import inputData
import time

start_time = time.time()

dataInput = inputData('data/day18.txt')
#dataInput = inputData('data/test18.txt')
#dataInput = inputData('data/test18-2.txt')

def dataArray():
    arrayOutput ={}
    for idx, i in enumerate(dataInput):
        for idy, point in enumerate(i):
            arrayOutput[idx, idy] = point
    return arrayOutput

def countOn(data):
    maxValx = max([i[0] for i in data.keys()])
    maxValy = max([i[1] for i in data.keys()])
    outputData = {}
    for i in data:
        count = 0
        for x in list(range(i[0] - 1, i[0] + 2)):
            for y in list(range(i[1] - 1, i[1] + 2)):
                if all([x > -1, x < maxValx + 1]):
                    if all([y > -1, y < maxValy + 1]):
                        if not(all([x == i[0], y == i[1]])):
                            if data[x , y] == "#":
                                count += 1
        outputData[i[0], i[1]] = count
    return outputData

def produceNewArray(countData, oldData):
    outputData = {}
    for i in countData:
        if countData[i] == 3:
            outputData[i[0], i[1]] = "#"
        elif countData[i] == 2:
            if oldData[i] == "#":
                outputData[i[0], i[1]] = "#"
            else:
                outputData[i[0], i[1]] = "."
        elif countData[i] != 2:
            outputData[i[0], i[1]] = "."
        else:
            outputData[i[0], i[1]] = "E"
    return outputData

def main(dt, loopcount):
    holdingArray = dt
    for i in range(loopcount):
        count = countOn(holdingArray)
        newArray = produceNewArray(count, holdingArray)
        holdingArray = newArray
    return list(newArray.values()).count("#")

def produceNewArray2(countData, oldData):
    outputData = {}
    maxValx = max([i[0] for i in countData.keys()])
    maxValy = max([i[1] for i in countData.keys()])
    for i in countData:
        if countData[i] == 3:
            outputData[i[0], i[1]] = "#"
        elif countData[i] == 2:
            if oldData[i] == "#":
                outputData[i[0], i[1]] = "#"
            else:
                outputData[i[0], i[1]] = "."
        elif countData[i] != 2:
            outputData[i[0], i[1]] = "."
        else:
            outputData[i[0], i[1]] = "E"
    #Hack to turn on lights
    outputData[0, 0] = "#"
    outputData[0, maxValy] = "#"
    outputData[maxValx, 0] = "#"
    outputData[maxValx, maxValy] = "#"
    return outputData

def main2(dt, loopcount):
    holdingArray = dt
    maxValx = max([i[0] for i in holdingArray.keys()])
    maxValy = max([i[1] for i in holdingArray.keys()])
    holdingArray[0, 0] = "#"
    holdingArray[0, maxValy] = "#"
    holdingArray[maxValx, 0] = "#"
    holdingArray[maxValx, maxValy] = "#"
    for i in range(loopcount):
        count = countOn(holdingArray)
        newArray = produceNewArray2(count, holdingArray)
        holdingArray = newArray
    return list(newArray.values()).count("#")


dt = dataArray()
answer1 = main(dt, 100)
answer2 = main2(dt, 100)

print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)

print('Took', round(time.time() - start_time,2), 'seconds to complete')