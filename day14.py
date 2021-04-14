#https://adventofcode.com/2015/day/14

from AoC import inputData
import time

start_time = time.time()

dataInput = inputData('data/day14.txt', t="rfa", r='(\d+)')
name = inputData('data/day14.txt', t="rex", r='^(\S+)')
#dataInput = inputData('data/test14.txt', t="rfa", r='(\d+)')
#name = inputData('data/test14.txt', t="rex", r='^(\S+)')

def assembleData():
    outputArray = {}
    for x in range(len(name)):
        outputArray[name[x][0]] = [int(dataInput[x][0]), int(dataInput[x][1]), int(dataInput[x][2]), 0, 0, 0, 0, 0]
    return outputArray

def main(data, val):
    #0speed, 1duration, 2rest, 3resting, 4moving, 5restval, 6outputVal, 7points
    for i in range(val):
        for rName in data:
            if data[rName][3] == 0:
                data[rName][4] += 1
                data[rName][6] += data[rName][0]
                if data[rName][4] >= data[rName][1]:
                    data[rName][3] = 1
                    data[rName][4] = 0
            elif data[rName][3] == 1:
                data[rName][5] += 1
                if data[rName][5] >= data[rName][2]:
                    data[rName][3] = 0
                    data[rName][5] = 0
        for rName in data:
            if data[rName][6] == max(list(zip(*data.values()))[6]):
                data[rName][7] += 1
    return max(list(zip(*data.values()))[6]), max(list(zip(*data.values()))[7])

data = assembleData()
answer1 = main(data, 2503)

print("Answer 1")
print(answer1[0])
print("Answer 2")
print(answer1[1])

print('Took', round(time.time() - start_time,2), 'seconds to complete')