#https://adventofcode.com/2015/day/10

import time
import re

start_time = time.time()

dataInput = "vzbxkghb"

def createAlphabet():
    num = 0
    alphabet = {}
    alphabetR = {}
    for i in range(97, 123):
        num += 1
        val = chr(i)
        alphabet[val] = num
        alphabetR[num] = val
    return alphabet, alphabetR

def increment(data):
    alphabet, alphabetR = createAlphabet()
    val = alphabet[data[-1:]]
    if val == 26:
        if len(data[0:-1]) > 0:
            x = increment(data[0:-1])
            val = 0
            output = x + alphabetR[val+1]
        else:
            val = 0
            output = 'a' + alphabetR[val + 1]
    else:
        output = data[0:-1] + alphabetR[val + 1]
    return output

def test1(passwd):
    matches = re.findall(r'abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz', passwd)
    if len(matches) > 0:
        return 1
    return -1

def test2(passwd):
    matches = re.findall(r'i|o|l', passwd)
    if len(matches) == 0:
        return 1
    return -1

def test3(passwd):
    matches = re.findall(r'([a-z])\1', passwd)
    if len(matches) == 2:
        return 1
    return -1

def alltests(passwd):
    a = test1(passwd)
    b = test2(passwd)
    c = test3(passwd)
    return a, b, c

def main(pswd):
    check = []
    while sum(check) != 3:
        pswd = increment(pswd)
        check = alltests(pswd)
    return pswd

answer1 = main(dataInput)
answer2 = main(answer1)

print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)

print('Took', round(time.time() - start_time,2), 'seconds to complete')