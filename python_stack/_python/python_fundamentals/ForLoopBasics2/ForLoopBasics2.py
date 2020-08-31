def biggerSize(list):
    for i in range(0,len(list)-1):
        if list[i] >= 0:
            list[i] = "big"
    return list
print(biggerSize([-1,3,5,-5]))

def countPositives(list):
    total=0
    for i in range(len(list)):
        if list[i] > 0:
            total+=1
    list[len(list)-1] = total
    return list

print(countPositives([-1,1,1,1]))
print(countPositives([1,6,-4,-2,-7,-2]))

def sumTotal(list):
    total=0
    for i in list:
        total += i
    return total

print(sumTotal([1,2,3,4]))
print(sumTotal([6,3,-2]))

def average(list):
    total=0
    for i in list:
        total+= i
    avg = total/len(list)
    return avg

print(average([1,2,3,4]))

def length(list):
    return len(list)

print(length([37,2,1,-9]))
print(length([]))

def minimum(list):
    if len(list)>0:
        lowest = list[0]
        for i in list:
            if i < lowest:
                lowest=i
            else:
                pass
        return lowest
    else:
        return False

print(minimum([37,2,1,-9]))
print(minimum([]))

def maximum(list):
    if len(list)>0:
        highest = list[0]
        for i in list:
            if i>highest:
                highest=i
            else:
                pass
        return highest
    else:
        return False

print(maximum([37,2,1,-9]))
print(maximum([]))

def ultimateAnalysis(list):
    dictionary = {'sumTotal': sumTotal(list), 'average': average(list), 'minimum': minimum(list), 'maximum':maximum(list), 'length':length(list)}
    return dictionary

print(ultimateAnalysis([37,2,1,-9]))

def reverseList(list):
    firstHalf = int(len(list)/2)
    for i in range(len(list)-1, firstHalf, -1):
        list.append(list[i])
        list.pop(i)
    for i in range(firstHalf, -1, -1):
        list.append(list[i])
        list.pop(i)
    return list

print(reverseList([37,2,1,-9]))