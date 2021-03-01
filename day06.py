#https://adventofcode.com/2015/day/6

from AoC import inputData
import time
import numpy as np

start_time = time.time()

dataInput = inputData('data/day06.txt', t="rex", r="(on|off|toggle) (\d*),(\d*) \w* (\d*),(\d*)")

def main():
    lightArray = np.empty((1000, 1000), int)
    lightArray2 = np.empty((1000, 1000), int)
    for i in dataInput:
        for x in range(int(i[1]), int(i[3])+1):
            for y in range(int(i[2]), int(i[4])+1):
                if i[0] == "on":
                    lightArray[x][y] = 1
                    lightArray2[x][y] = lightArray2[x][y] + 1
                elif i[0] == "off":
                    lightArray[x][y] = 0
                    lightArray2[x][y] = lightArray2[x][y] - 1
                    if lightArray2[x][y] < 0:
                        lightArray2[x][y] = 0
                elif i[0] == "toggle":
                    lightArray[x][y] = 1 - lightArray[x][y]
                    lightArray2[x][y] = lightArray2[x][y] + 2
    return np.sum(lightArray), np.sum(lightArray2)

answer = main()
print("Answer 1")
print(answer[0])
print("Answer 2")
print(answer[1])

print('Took', round(time.time() - start_time,2), 'seconds to complete')
#First personal attempt 27.25 seconds