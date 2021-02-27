from AoC import inputData

dataSet = 0

if dataSet == 0:
    dataInput = inputData('data/day02.txt',t="rex",r="^(\d*)x(\d*)x(\d*)$")
if dataSet == 1:
    dataInput = inputData('data/test02.txt',t="rex",r="^(\d*)x(\d*)x(\d*)$")

def main():
    totalBoxArea = 0
    totalRibbon = 0
    for data in dataInput:
        dataInt = [int(i) for i in data]
        length, width, height = dataInt
        dataSort = [length, width, height]
        dataSort.sort()
        low1 = dataSort[0]
        low2 = dataSort[1]
        boxSide = [(length*width),(width*height),(height*length)]
        ribbon = ((low1 + low1 + low2 + low2) + (length * width * height))
        boxArea = ((2 * boxSide[0]) + (2 * boxSide[1]) + (2 * boxSide[2]) + min(boxSide))
        totalRibbon = totalRibbon + ribbon
        totalBoxArea = totalBoxArea + boxArea
    return totalBoxArea,totalRibbon

data = main()
print("Answer 1")
print(data[0])
print("Answer 2")
print(data[1])