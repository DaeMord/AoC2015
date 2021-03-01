#https://adventofcode.com/2015/day/5

from AoC import inputData
import re

dataInput = inputData('data/day05.txt')
#dataInput = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
#dataInput = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']

def main():
    nice = 0
    nice2 = 0
    for i in dataInput:
        data = analyseData(i)
        if data[2] == 0 and data[1] > 0 and data[0] >= 3:
            nice += 1
        if data[3] == 1 and data[4] >= 1:
            nice2 += 1
    return nice, nice2

def duplicateEntries(data):
    for i in range(len(data)-1):
        check = data[i] + data[i + 1]
        rex = re.compile(check)
        if len(rex.findall(data)) == 2:
            return 1
    return -1


def analyseData(data):
    vowelCount = len(re.findall('a|e|i|o|u', data))
    duplicateCount = len(re.findall(r"([a-z])\1", data))
    naughtyCount = len(re.findall('ab|cd|pq|xy', data))
    part2part1 = duplicateEntries(data)
    part2DuplicateCount = len(re.findall(r"([a-z]).\1", data))
    return vowelCount, duplicateCount, naughtyCount, part2part1, part2DuplicateCount


answer = main()
print("Answer 1")
print(answer[0])
print("Answer 2")
print(answer[1])