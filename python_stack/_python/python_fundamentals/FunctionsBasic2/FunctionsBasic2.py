def countdown(x):
    newArr = []
    for y in range(x, -1, -1):
        newArr.append(y)
    return newArr

print(countdown(5))

def printAndReturn(list):
    print(list[0])
    return list[1]

print(printAndReturn([1,2]))

def firstPlusLength(list):
    return list[0] + len(list)

print(firstPlusLength([1,2,3,4,5]))

def valuesGreaterThanSecond(list):
    if len(list)>=3:
        newList = []
        index = list[2]
        for i in list:
            if i>=index:
                newList.append(i)
            else:
                pass
        print(index)
        return newList
    else:
        return False

print(valuesGreaterThanSecond([5,2,3,2,1,4]))
print(valuesGreaterThanSecond([3]))

def thisLengthThatValue(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList

print(thisLengthThatValue(4,7))
print(thisLengthThatValue(6,2))
