#https://adventofcode.com/2015/day/6

from AoC import inputData
import time

start_time = time.time()

dataInput = inputData('data/day06.txt', t="rex", r="(on|off|toggle) (\d*),(\d*) \w* (\d*),(\d*)")

def main():
    lightArray = [[0 for x in range(1000)] for y in range(1000)]
    lightArray2 = [[0 for x in range(1000)] for y in range(1000)]

    for i in dataInput:
        for x in range(int(i[1]), int(i[3])+1):
            for y in range(int(i[2]), int(i[4])+1):
                if i[0] == "on":
                    lightArray[x][y] = 1
                    lightArray2[x][y] += 1
                elif i[0] == "off":
                    lightArray[x][y] = 0
                    if lightArray2[x][y] > 0:
                        lightArray2[x][y] -= 1
                elif i[0] == "toggle":
                    lightArray[x][y] = 1 - lightArray[x][y]
                    lightArray2[x][y] += 2
    return sum(map(sum,lightArray)), sum(map(sum,lightArray2))

answer = main()
print("Answer 1")
print(answer[0])
print("Answer 2")
print(answer[1])

print('Took', round(time.time() - start_time,2), 'seconds to complete')
#First personal attempt 27.25 seconds
#Dont Use a numpy array for this, 3.47 seconds