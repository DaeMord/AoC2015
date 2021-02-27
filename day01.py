from AoC import inputData

dataInput = inputData('data/day01.txt')

def main():
    output = 0
    loop = 0
    basement = 0
    for i in dataInput[0]:
        if i == "(":
            output = output + 1
        if i == ")":
            output = output - 1
        loop = loop + 1
        if basement == 0 and output < 0:
            basement = loop
    returnOut = [output,basement]
    return returnOut

data = main()
answer1,answer2 = data[0],data[1]
print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)