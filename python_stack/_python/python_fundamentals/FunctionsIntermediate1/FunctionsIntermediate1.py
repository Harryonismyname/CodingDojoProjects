import random
def randInt(min= 0 , max= 100 ):
    if min > max:
        temp= min
        min = max
        max = temp
    num = random.random()*(max-min)+min
    return num
print(randInt())# should print a random integer between 0 to 100
print(randInt(max=50))# should print a random integer between 0 to 50
print(randInt(min=50))# should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
"""
def basicRandITest():
    for x in range(101):
        basicRandI = randInt()
        if basicRandI > 100 or basicRandI < 0:
            print("RandI Error!")
        else:
            pass

basicRandITest()

def maxRandITest(max):
    for x in range(max+1):
        maxRandI = randInt(max)
        if maxRandI > max or maxRandI < 0:
            print("RandI Error!")

def randITester(a=0, b=100):
    if a>b:
        temp=a
        a=b
        b=temp
    for x in range(a, b+1):
        randI = randInt(min=a, max=x)
        if randI > b or randI < a:
            print("RandI Error!")

randITester(a=200, b=40)
"""
