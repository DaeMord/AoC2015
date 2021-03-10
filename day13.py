#https://adventofcode.com/2015/day/13

from AoC import inputData
import time
import itertools
import numpy as np

start_time = time.time()

dataInput = inputData('data/day13.txt', t="rex", r='^(\w*) would (gain|lose) (\d+).* to (\w*)')
#dataInput = inputData('data/test13.txt', t="rex", r='^(\w*) would (gain|lose) (\d+).* to (\w*)')

def dataStrip(data):
    names = set()
    namesKeys = {}
    for i in data:
        names.update([i[0], i[3]])
    k = 0
    for i in names:
        namesKeys[i] = k
        k += 1
    return names, namesKeys

def dataConvert(data,keys):
    newArray = []
    for i in data:
        if i[1] == "lose":
            number = -int(i[2])
        else:
            number = int(i[2])
        newArray.append((keys[i[0]], keys[i[3]], number))
    return newArray

def main(data):
    dataStripped = dataStrip(data)
    dataConverted = dataConvert(data, dataStripped[1])
    array = np.zeros(shape=[len(dataStripped[1]), len(dataStripped[1])])
    for i in dataConverted:
        array[i[0]][i[1]] += i[2]
        array[i[1]][i[0]] += i[2]
    bruteForce = list(range(len(dataStripped[1])))
    bruteForceArray = itertools.permutations(bruteForce, len(dataStripped[1]))
    outputDict = {}
    output = 0
    newArray = []
    for i in bruteForceArray:
        for x in range(len(i) - 1):
            output += array[i[x], i[x + 1]]
        newArray.append(array[i[-1], i[0]])
        output += array[i[-1], i[0]]
        outputDict[i] = output
        output = 0
    permutation = max(outputDict, key=outputDict.get)
    return outputDict[permutation]

def modifyData(data):
    dataStripped = dataStrip(data)
    arrayToMerge = []
    for i in dataStripped[0]:
        arrayToMerge.append(("Peter", "gain", "0", i))
        arrayToMerge.append((i, "gain", "0", "Peter"))
    return data + arrayToMerge

answer1 = main(dataInput)
answer2 = main(modifyData(dataInput))

print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)

print('Took', round(time.time() - start_time,2), 'seconds to complete')


