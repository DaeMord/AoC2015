#https://adventofcode.com/2015/day/16

from AoC import inputData
import time
import itertools

start_time = time.time()

dataInput = inputData('data/day17.txt', t="int")

def main(valueToReach, data):
    dataArray = [z for i in range(len(data)) for z in itertools.combinations(data, i) if sum(z) == valueToReach]
    ans2 = len([x for x in dataArray if len(x) == min([len(x) for x in dataArray])])
    ans1 = len(dataArray)
    return ans1, ans2

answer1 = main(100, dataInput)

print("Answer 1")
print(answer1[0])
print("Answer 2")
print(answer1[1])

print('Took', round(time.time() - start_time,2), 'seconds to complete')