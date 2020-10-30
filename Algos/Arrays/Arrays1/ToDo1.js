var arr = [2,3,4]
var val = 1
function PushFront(arr, val)
{
    for(var i =arr.length-1; i>-1; i--)
    {
        arr[i+1]= arr[i]
    }
    arr[0]= val
    return arr
}
console.log(PushFront(arr,val))

var arr = [1,2,3,4]

function PopFront(arr)
{
    var front= arr[0]
    var newArr = []
    for(var i=0; i<arr.length-1; i++)
    {
        newArr[i]= arr[i+1]
    }
    var show= [front, newArr]
    return show
}

console.log(PopFront(arr))

var arr = [1,2,3,4,5,7,8,9]
var index = 5
var val = 6

function insertAt(arr, index, val)
{
    for(var i = arr.length-1; i>index-1; i--)
    {
        arr[i+1]=arr[i]
    }
    arr[index]=val
    return arr
}

console.log(insertAt(arr, index, val))

var arr = [1,2,3,4,5,6,7,8,8,9]
var index = 7

function removeAt(arr, index)
{
    var val= arr[index]
    var newArr = []
    for(var i= 0; i<index; i++)
    {
        newArr[i]=arr[i]
        for (var v = index; v<arr.length-1; v++)
        {
            newArr[v]= arr[v+1]
        }
    }
    var show = [val, newArr]
    return show
}

console.log(removeAt(arr, index))

var arr = [ 'on','Harry', 'Elderhale', 'Vincent', 'Grainstone', 'Morgana']
var arr2= ['on', 'Harry', 'Elderhale', 'Vincent', 'Shoe']

function swapPairs(arr)
{
    for(var i=0; i<arr.length-1; i+=2)
    {
        if(arr.length % 2 != 0 && i==arr.length-1){}
        else
        {
            var present= arr[i]
            arr[i] = arr[i+1]
            arr[i+1]= present
        }
    }
    return arr
}

console.log(swapPairs(arr))
console.log(swapPairs(arr2))

var arr = [1,1,2,3,4,5,5,6,7,8,9]

function removeDupes(arr)
{
    var newArr = []
    var num2 = 0
    for(var i=0; i<arr.length; i++)
    {
        if(arr[i]==arr[i+1]){}
        else
        {
            newArr[num2]= arr[i]
            num2++
        }
    }
    return newArr
}

console.log(removeDupes(arr))
