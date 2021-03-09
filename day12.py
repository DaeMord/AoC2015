#https://adventofcode.com/2015/day/12

from AoC import inputData
import time
import re

start_time = time.time()

dataInput = inputData('data/day12.txt')

def part1(data):
    return sum(map(int, re.findall(r'(-?\d+)', data)))

def part2(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(part2(i) for i in data)
    elif isinstance(data, dict):
        if "red" in data.values():
            return 0
        else:
            return sum(part2(i) for i in data.values())
    return 0

answer1 = part1(dataInput[0])
answer2 = part2(eval(dataInput[0]))

print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)

print('Took', round(time.time() - start_time,2), 'seconds to complete')