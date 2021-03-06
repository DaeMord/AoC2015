#https://adventofcode.com/2015/day/10

import time
from itertools import groupby

start_time = time.time()

dataInput = "1113122113"
#dataInput = "1"

def inputString(data):
    return ''.join(str(len(list(count))) + val for val, count in groupby(data))

def main(dataInp, loopCount):
    input = dataInp
    for i in range(loopCount):
        input = inputString(input)
    return input

print("Answer 1")
print(len(main(dataInput, 40)))

print("Answer 2")
print(len(main(dataInput, 50)))

print('Took', round(time.time() - start_time,2), 'seconds to complete')
