import re
import math

def test():
    print("Test")

def inputData(filename,t="str",r=""):
    """
    Input data from filename
    type variables
    str = string
    int = numbers
    rex = regex, r= to set
    rfa = refex Find all r= to set
    """
    dataoutput = []
    fileName = filename
    regex = re.compile(r)
    with open(fileName) as f:
        for line in f:
            if t == 'str':
                dataoutput.append(line.strip())
            elif t == 'int':
                dataoutput.append(int(line.strip()))
            elif t == 'rex':
                dataoutput.append(regex.search(line.strip()).groups())
            elif t == 'rfa':
                dataoutput.append(regex.findall(line.strip()))

    return dataoutput

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point
    angle = math.radians(angle)

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return round(qx), round(qy)

def printArray(inputArray):
    for x in inputArray:
        for y in x:
            print(y,end='')
        print()
