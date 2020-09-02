arr = [6,5,3,1,8,7,2,4,4,56,2,7,7,8,8,9,9,4,354645,6345,63,4,563,456,3546,345,6345,6,345,73,74,567,456,745,674,567]

def insertionSort(arr):
    for i in range(len(arr)):
        index = arr[i]
        if arr[i]<arr[i-1]:
            for j in range(i,0,-1):
                if index<arr[j-1]:
                    arr[j],arr[j-1] = arr[j-1],index
    return(arr)

print(insertionSort(arr))

