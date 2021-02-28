#https://adventofcode.com/2015/day/4

import hashlib
import time

start_time = time.time()

inputKey = "bgvyzdsv"

def main(secretKey):
    hash = secretKey
    i = 0
    answer1 = 0
    hashCheck = hashlib.md5(hash.encode()).hexdigest()
    while not hashCheck[:6] == '000000':
        if answer1 == 0 and hashCheck[:5] == '00000':
               answer1 = i
        i += 1
        hashCheck = hashlib.md5((secretKey + str(i)).encode()).hexdigest()
    return answer1, i

answer = main(inputKey)
print("Answer 1")
print(answer[0])
print("Answer 2")
print(answer[1])

print('Took', round(time.time() - start_time,2), 'seconds to complete')

