var arr = [4,2,1,3,5]
function minToFront(arr)
{
    var min = arr[0]
    var newArr = []
    var x = 0
    var i = 0
    while(x<2)
    {
        if(x==0)
        {
            if(i>arr.length)
            {
                newArr[0]=min
                x++
                i=0
                continue
            }
            if(arr[i]<min)
            {
                min= arr[i]
            }
            i++
        }
        if(x==1)
        {
            if(i>arr.length-1)
            {
                x++
                i=0
                continue
            }
            if(arr[i]>min)
            {
                newArr[newArr.length]=arr[i]
            }
            
            i++
        }
    }
    return newArr
}
console.log(minToFront(arr))