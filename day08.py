#https://adventofcode.com/2015/day/8

from AoC import inputData
import time

start_time = time.time()

dataInput = inputData('data/day08.txt')
#dataInput = inputData('data/test08.txt')

def main():
    dataRaw = 0
    dataProcessed = 0
    for data in dataInput:
        dataRaw += len(data)
        dataProcessed += len(eval(data))
    return dataRaw - dataProcessed

def main2():
    dataRaw = 0
    dataProcessed = 0
    for data in dataInput:
        dataRaw += len(data)
        outputData = data.replace('\\', '\\\\')
        outputData = outputData.replace('"', '\\"')
        dataProcessed += len(outputData)
        dataProcessed += 2
    return dataProcessed - dataRaw

print("Answer 1")
print(main())
print("Answer 2")
print(main2())

print('Took', round(time.time() - start_time,2), 'seconds to complete')
#Part 1
#Guess 1329 too low
#Guess 1360 too high
#Guess 1349 too high