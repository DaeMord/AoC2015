#https://adventofcode.com/2015/day/16

from AoC import inputData
import time

start_time = time.time()

dataInput = inputData('data/day16.txt', t="rex", r='Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')

MFCSAM = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

def buildData(data):
    outputData = {}
    for i in data:
        outputData[int(i[0])] = {}
        outputData[int(i[0])][i[1]] = int(i[2])
        outputData[int(i[0])][i[3]] = int(i[4])
        outputData[int(i[0])][i[5]] = int(i[6])
    return outputData

def main(input):
    auntSue = buildData(input)
    part1 = {}
    part2 = {}
    for i in auntSue:
        if len(auntSue[i].items() & MFCSAM.items()) == 3:
            part1[i] = auntSue[i]
        if "cats" in set(auntSue[i].keys()):
            if auntSue[i]['cats'] > MFCSAM['cats']:
                auntSue[i]['cats'] = MFCSAM['cats']
        if "trees" in set(auntSue[i].keys()):
            if auntSue[i]['trees'] > MFCSAM['trees']:
                auntSue[i]['trees'] = MFCSAM['trees']
        if "pomeranians" in set(auntSue[i].keys()):
            if auntSue[i]['pomeranians'] < MFCSAM['pomeranians']:
                auntSue[i]['pomeranians'] = MFCSAM['pomeranians']
        if "goldfish" in set(auntSue[i].keys()):
            if auntSue[i]['goldfish'] < MFCSAM['goldfish']:
                auntSue[i]['goldfish'] = MFCSAM['goldfish']
        if len(auntSue[i].items() & MFCSAM.items()) == 3:
            part2[i] = auntSue[i]
    return list(part1.keys())[0], list(part2.keys())[0]

answer1 = main(dataInput)

print("Answer 1")
print(answer1[0])
print("Answer 2")
print(answer1[1])

print('Took', round(time.time() - start_time,2), 'seconds to complete')