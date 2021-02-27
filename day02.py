#https://adventofcode.com/2015/day/2

from AoC import inputData

dataSet = 0

if dataSet == 0:
    dataInput = inputData('data/day02.txt', t="rex", r="^(\d*)x(\d*)x(\d*)$")
if dataSet == 1:
    dataInput = inputData('data/test02.txt', t="rex", r="^(\d*)x(\d*)x(\d*)$")

def main():
    totalBoxArea = 0
    totalRibbon = 0
    for data in dataInput:
        length, width, height = [int(i) for i in data]
        boxSide = [(length * width), (width * height), (height * length)]
        totalBoxArea = totalBoxArea + sum((2 * bA for bA in boxSide)) + min(boxSide)
        totalRibbon = totalRibbon + (2 * min((length + width), (width + height), (height + length)) + (length * width * height))
    return totalBoxArea, totalRibbon

data = main()
print("Answer 1")
print(data[0])
print("Answer 2")
print(data[1])