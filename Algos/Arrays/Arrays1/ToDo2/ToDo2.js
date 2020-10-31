var arr=[1,2,3,4,5,6,7,8,9]

function reverse(arr)
{
    for(var i=0; i<arr.length/2; i++)
    {
        var holder = arr[i]
        arr[i]= arr[arr.length-1-i]
        arr[arr.length-1-i]=holder
    }
    return arr
}

console.log(reverse(arr))

var arr=[2,3,4,5,6,1]
var arr2=[2,3,4,5,1]
var shiftBy = 1
var shiftBy2 = -4

function rotateArr(arr, shiftBy)
{
    if(shiftBy>0)
    {
        for(var x=0; x<shiftBy; x++)
        {
            var end= arr[arr.length-1]
            for(var i=arr.length-1; i>0; i--)
            {
                arr[i]=arr[i-1]
            }
            arr[0]=end
        }
    }
    else
    {
        for (var x = 0; x>shiftBy; x--)
        {
            var front = arr[0]
            for(var i=0; i<arr.length-1; i++)
            {
                arr[i]= arr[i+1]
            }
            arr[arr.length-1] = front
            console.log(arr)
        }
    }
    return arr
}

console.log(rotateArr(arr, shiftBy))
console.log(rotateArr(arr2, shiftBy2))

var arr=[1,3,4,5,1,3,1,41,3,5,51,1,3,4,5,6]
var min=2
var max=10

function filterRange(arr, min, max)
{
    for(var i =0; i<arr.length; i++)
    {
        if(arr[i]<max && arr[i]>min)
        {
            for(var j=i; j<arr.length-1; j++)
            {
                arr[j]= arr[j+1]
            }
            arr.length = arr.length-1
            i--
        }
        
    }
}
filterRange(arr, min, max)
console.log(arr)

var arr= [1,2,3]
var arr2 = [4,5,6]

function arrConcat(arr1,arr2)
{
    var newArr =[]
    var i = 0
    var j = 0
    while(j<2)
    {
        if(j==0)
        {
            if(i>arr1.length-1)
            {
                i=0
                j++
                continue
            }
            newArr[newArr.length]= arr1[i]
            i++
        }
        if(j==1)
        {
            if(i>arr2.length-1)
            {
                i=0
                j++
                continue
            }
            newArr[newArr.length]=arr2[i]
            i++
        }
    }
    return newArr
}

console.log(arrConcat(arr,arr2))
