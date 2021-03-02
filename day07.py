#https://adventofcode.com/2015/day/7

from AoC import inputData
import time
import re
import copy

start_time = time.time()

dataInput = inputData('data/day07.txt', t="rex", r="(.*) -> (.*)")
#dataInput = inputData('data/test07.txt', t="rex", r="(.*) -> (.*)")
dataInput1 = copy.deepcopy(dataInput)
dataInput2 = copy.deepcopy(dataInput)

def main(dataInput):
    memory = {}
    arrayPos = 0
    while len(dataInput) > 0:
        if not any(re.findall(r'AND|OR|NOT|LSHIFT|RSHIFT', dataInput[arrayPos][0])):
            if dataInput[arrayPos][0].isnumeric():
                memory[dataInput[arrayPos][1]] = int(dataInput[arrayPos][0])
                del dataInput[arrayPos]
                arrayPos = 0
            elif dataInput[arrayPos][0] in memory:
                memory[dataInput[arrayPos][1]] = int(memory[dataInput[arrayPos][0]])
                del dataInput[arrayPos]
                arrayPos = 0
            else:
                arrayPos += 1
        elif any(re.findall(r'AND|OR', dataInput[arrayPos][0])):
            memoryCheck = re.split(' AND | OR ', dataInput[arrayPos][0])
            if any([memoryCheck[0] in memory, memoryCheck[0].isnumeric()]) and any([(memoryCheck[1] in memory), memoryCheck[1].isnumeric()]):
                if memoryCheck[0].isnumeric():
                    var1 = memoryCheck[0]
                else:
                    var1 = memory[memoryCheck[0]]
                if "AND" in dataInput[arrayPos][0]:
                    memory[dataInput[arrayPos][1]] = int(var1) & int(memory[memoryCheck[1]])
                elif "OR" in dataInput[arrayPos][0]:
                    memory[dataInput[arrayPos][1]] = int(memory[memoryCheck[0]]) | int(memory[memoryCheck[1]])
                del dataInput[arrayPos]
                arrayPos = 0
            else:
                arrayPos += 1
        elif any(re.findall(r'LSHIFT|RSHIFT', dataInput[arrayPos][0])):
            memoryCheck = re.split(' LSHIFT | RSHIFT ', dataInput[arrayPos][0])
            if memoryCheck[0] in memory:
                if "LSHIFT" in dataInput[arrayPos][0]:
                    memory[dataInput[arrayPos][1]] = int(memory[memoryCheck[0]]) << int(memoryCheck[1])
                elif "RSHIFT" in dataInput[arrayPos][0]:
                    memory[dataInput[arrayPos][1]] = int(memory[memoryCheck[0]]) >> int(memoryCheck[1])
                del dataInput[arrayPos]
                arrayPos = 0
            else:
                arrayPos += 1
        elif any(re.findall(r'NOT', dataInput[arrayPos][0])):
            memoryCheck = re.split('NOT ', dataInput[arrayPos][0])
            if memoryCheck[1] in memory:
                if "NOT" in dataInput[arrayPos][0]:
                    memory[dataInput[arrayPos][1]] = ~int(memory[memoryCheck[1]]) & 0xffff
                del dataInput[arrayPos]
                arrayPos = 0
            else:
                arrayPos += 1
        else:
            arrayPos += 1
    return(memory["a"])

def bugfix(dataInput):
    pos = 0
    for i in dataInput:
        if i[1] == "b":
            bpos = pos
        pos += 1
    dataInput[bpos] = ('16076', 'b')

answer1 = main(dataInput1)
print("Answer 1")
print(answer1)
bugfix(dataInput2)
answer2 = main(dataInput2)
print("Answer 2")
print(answer2)

print('Took', round(time.time() - start_time,2), 'seconds to complete')