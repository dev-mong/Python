import math

def getCircleArea(radius = 0):
    return math.pow(radius,2) * math.pi

def getDonutArea(r1,r2):

    area1 = getCircleArea(r1)
    area2 = getCircleArea(r2)

    return abs(area1 - area2)

if __name__ == "__main__":

    result = getDonutArea(4,10)
    print(result)