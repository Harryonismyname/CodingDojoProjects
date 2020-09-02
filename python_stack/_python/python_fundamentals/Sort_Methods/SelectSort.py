arr = [8,0,2,3,5,1,6,7,8,3,1,23,4,4]

def selectSort(arr):
    for i in range(len(arr)-1):
        index= i
        for j in range(i, len(arr)):
            if arr[j]<arr[index]:
                index = j
        arr[i],arr[index]=arr[index],arr[i]
    return arr


print(selectSort(arr))
