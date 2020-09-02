arr = [1,5,3,2,0,8]

def bubbleSort(arr):
    evals = 0
    for x in range(len(arr)-1):
        for i in range(len(arr)-1-x):
            if arr[i]> arr[i+1]:
                arr[i], arr[i+1] =arr[i+1], arr[i]
            evals+=1
    print('total evals', evals)
    return arr

print(bubbleSort(arr))