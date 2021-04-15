#https://adventofcode.com/2015/day/15

from AoC import inputData
import time
import itertools

start_time = time.time()

dataInput = inputData('data/day15.txt', t="rex", r='(\w+).+?(-{0,1}\d+).+?(-{0,1}\d+).+?(-{0,1}\d+).+?(-{0,1}\d+).+?(-{0,1}\d+)')
#dataInput = inputData('data/test15.txt', t="rex", r='(\w+).+?(-{0,1}\d+).+?(-{0,1}\d+).+?(-{0,1}\d+).+?(-{0,1}\d+).+?(-{0,1}\d+)')
#Capacity 1 Durability 2 Flavour 3 Texture 4 Calories 5

def main():
    outputArray = []
    outputCalorie = []
    for i in createCalcArray(len(dataInput), 100):
        capacity = 0
        durability = 0
        flavour = 0
        texture = 0
        calories = 0
        for count, x in enumerate(i):
            capacity += int(dataInput[count][1]) * x
            durability += int(dataInput[count][2]) * x
            flavour += int(dataInput[count][3]) * x
            texture += int(dataInput[count][4]) * x
            calories += int(dataInput[count][5]) * x
        capacity = max(capacity, 0)
        durability = max(durability, 0)
        flavour = max(flavour, 0)
        texture = max(texture, 0)
        score = capacity * durability * flavour * texture
        outputArray.append(score)
        if calories == 500 and score > 0:
            outputCalorie.append(score)
    return max(outputArray), max(outputCalorie)

def createCalcArray(var, addto):
    for output in itertools.product(range(0, addto + 1), repeat=var):
        if sum(output) == 100:
            yield output

answer1 = main()

print("Answer 1")
print(answer1[0])
print("Answer 2")
print(answer1[1])

print('Took', round(time.time() - start_time,2), 'seconds to complete')