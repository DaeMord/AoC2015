#https://adventofcode.com/2015/day/8

from AoC import inputData
import time
import codecs

start_time = time.time()

dataInput = inputData('data/day08.txt')
#dataInput = inputData('data/test08.txt')

def main():
    dataRaw = 0
    dataProcessed = 0
    for data in dataInput:
        dataRaw += len(data)
        outputData = ""
        i = 0
        while i < (len(data)):
            if data[i] == '"':
                i += 1
            elif data[i] == "\\":
                if data[i+1] == '"':
                    outputData = outputData + (data[i+1])
                    i += 2
                elif data[i+1] == "\\":
                    outputData = outputData + (data[i+1])
                    i += 2
                elif data[i+1] == "x":
                    outputData = outputData + codecs.decode(data[i:i+4], 'unicode_escape')
                    i += 4
            else:
                outputData = outputData + data[i]
                i += 1
        dataProcessed += len(outputData)
    return dataRaw - dataProcessed

def main2():
    dataRaw = 0
    dataProcessed = 0
    for data in dataInput:
        dataRaw += len(data)
        outputData = '"'
        i = 0
        while i < (len(data)):
            if data[i] == '"':
                outputData = outputData + '\\"'
                i += 1
            elif data[i] == "\\":
                outputData = outputData + '\\' + '\\'
                i += 1
            else:
                outputData = outputData + data[i]
                i += 1
        outputData = outputData + '"'
        dataProcessed += len(outputData)
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