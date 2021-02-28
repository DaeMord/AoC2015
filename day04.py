#https://adventofcode.com/2015/day/4

import hashlib
import re

inputKey = "bgvyzdsv"

def main(secretKey,rex):
    hash = secretKey
    i = 0
    while not (re.match(rex,hashlib.md5(hash.encode()).hexdigest())):
        i += 1
        hash = secretKey + str(i)
    return i

answer1 = main(inputKey,"^00000")
print("Answer 1")
print(answer1)
answer2 = main(inputKey,"^000000")
print("Answer 2")
print(answer2)


