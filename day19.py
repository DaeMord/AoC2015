#https://adventofcode.com/2015/day/19

from AoC import inputData
import time

start_time = time.time()

dataInput = inputData('data/day19.txt')
dataString = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"
#dataInput = inputData('data/test19.txt')
#dataString = "HOH"
#dataString = "HOHOHO"
#dataInput = ['H => OO']
#dataString = "H2O"
#dataInput = ['RnC => 11']
#dataString = "RnCaCaCaSiRnBPTiMgArSiRnSiRnMgA"

def main1():
    output = []
    for i in dataInput:
        i = i.split(" => ")
        pos = ([m for m in range(len(dataString)) if dataString.startswith(i[0], m)])
        for idx in pos:
            newString = (dataString[:idx] + i[1] + dataString[idx + len(i[0]):])
            output.append(newString)
    return output

runMain = main1()
answer1 = len(set(runMain))
answer2 = 1

print("Answer 1")
print(answer1)
#Guess 1 .. 207 too low
#Guess 2 .. 638 too high
#Guess 3 .. 613 too high
print("Answer 2")
print(answer2)

print('Took', round(time.time() - start_time,2), 'seconds to complete')