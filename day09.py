#https://adventofcode.com/2015/day/9

from AoC import inputData,printArray
import time
import numpy as np
import itertools

start_time = time.time()

dataInput = inputData('data/day09.txt', t = "rex" ,r = "(\w*) to (\w*) = (\d*)")
#dataInput = inputData('data/test09.txt', t = "rex" ,r = "(\w*) to (\w*) = (\d*)")

def dataStrip(data):
    locations = set()
    locationKeys = {}
    for i in data:
        locations.update([i[0], i[1]])
    k = 0
    for i in locations:
        locationKeys[i] = k
        k += 1
    return locations, locationKeys

def dataConvert(data,keys):
    newArray = []
    for i in data:
        newArray.append((keys[i[0]], keys[i[1]], int(i[2])))
    return newArray

data = dataInput
dataStripped = dataStrip(dataInput)
dataConverted = dataConvert(data,dataStripped[1])
bruteForce = list(range(len(dataStripped[1])))
bruteForceArray = itertools.permutations(bruteForce, len(dataStripped[1]))
reverse = dict(map(reversed, dataStripped[1].items()))
data2 = []
for i in dataConverted:
    data2.append((i[2]))
maxData = max(data2)
array = np.zeros(shape=[len(dataStripped[1]), len(dataStripped[1])])
array2 = np.zeros(shape=[len(dataStripped[1]), len(dataStripped[1])])
for i in dataConverted:
    array[i[0]][i[1]] = i[2]
    array[i[1]][i[0]] = i[2]
outputDict = {}
output = 0
for i in bruteForceArray:
    for x in range(len(i)-1):
        output += array[i[x],i[x+1]]
    outputDict[i]=output
    output = 0
reverseBrute = dict(map(reversed, outputDict.items()))
permutation = min(outputDict, key=outputDict.get)

print("Answer 1")
print(min(reverseBrute))
print("Answer 2")
print(max(reverseBrute))

print('Took', round(time.time() - start_time,2), 'seconds to complete')

# London > Dublin > Belfast
#207 Right answer 0.0 seconds BOOSH
#9223372036854775807 too high for part 2