#https://adventofcode.com/2015/day/5

from AoC import inputData
import re
import time

start_time = time.time()

dataInput = inputData('data/day05.txt')

def main():
    nice = 0
    nice2 = 0
    for i in dataInput:
        if len(re.findall('ab|cd|pq|xy', i)) == 0 and len(re.findall(r"([a-z])\1", i)) > 0 and len(re.findall('a|e|i|o|u', i)) >= 3:
            nice += 1
        if duplicateEntries(i) == 1 and len(re.findall(r"([a-z]).\1", i)) >= 1:
            nice2 += 1
    return nice, nice2

def duplicateEntries(data):
    for i in range(len(data)-1):
        check = data[i] + data[i + 1]
        rex = re.compile(check)
        if len(rex.findall(data)) == 2:
            return 1
    return -1

answer = main()
print("Answer 1")
print(answer[0])
print("Answer 2")
print(answer[1])

print('Took', round(time.time() - start_time,2), 'seconds to complete')