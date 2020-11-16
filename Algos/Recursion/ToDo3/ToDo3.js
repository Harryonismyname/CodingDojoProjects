function rBinarySearch(arr, value, index=0)
{
    if(index<arr.length-1)
    {
        if(value == arr[index])
        {
            return true
        }
        else if(value != arr[index])
        {
            return rBinarySearch(arr, value, index+1)
        }
    }
    else
    {
        return false
    }
}
console.log(rBinarySearch([1,3,5,6],4))
console.log(rBinarySearch([4,5,6,8,12],5))

function rGCF(num1, num2)
{
    if(num1==num2)
    {
        return num1
    }
    if(num1>num2)
    {
        if(num1%num2!=0)
        {
            return rGCF(num1-num2, num2)
        }
        else
        {
            return num2
        }
    }
    if(num1<num2)
    {
        if(num2%num1!=0)
        {
            return rGCF(num1,num2-num1)
        }
        else
        {
            return num1
        }
    }
}

console.log(rGCF(90,100))
console.log(rGCF(123456,987654))

function tarai(x,y,z)
{
    if(x<=y)
    {
        return y
    }
    else
    {
        return tarai(tarai(x-1,y,z),tarai(y-1,z,x),tarai(z-1,x,y))
    }
}

tarai(10,2,9)