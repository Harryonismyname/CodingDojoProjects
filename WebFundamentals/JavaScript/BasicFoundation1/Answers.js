//====================Question 1====================\\
function numberClimb()
{
    console.log("This is question 1")
    var newArr = []
    for(var i = 1; i<=255; i++)
    {
        newArr.push(i)
    }
    return newArr
}
console.log(numberClimb())

//====================Question 2====================\\
function toOneThousand()
{
    console.log("This is question 2")
    var sum = 0
    for(var i=1; i<=1000; i++)
    {
        if(i%2==0)
        {
            sum +=i
        }
    }
    return sum
}
console.log(toOneThousand())

//====================Question 3====================\\
function oddFiveThousand()
{
    console.log("This is question 3")
    var sum = 0
    for(var i= 0; i<=5000; i++)
    {
        if(i%2!=0)
        {
            sum+=i
        }
    }
    return sum
}
console.log(oddFiveThousand())

//====================Question 4====================\\
var madeUpArr = [2,4,6,8,56,54,3,2,4,5,6,7]
function iterArr(arr=[])
{
    console.log("This is question 4")
    var sum = 0;
    for(var i=0; i<arr.length; i++)
    {
        sum+=arr[i];
    }
    return sum;
}
console.log(iterArr(madeUpArr))

//====================Question 5====================\\
function findMax(arr=[])
{
    console.log("This is question 5")
    var max= arr[0];
    for(var i = 0; i<arr.length; i++)
    {
        if(max>arr[i])
        {
            max=arr[i];
        }
    }
    return max;
}
console.log(findMax(madeUpArr))

//====================Question 6====================\\
function findAverage(arr=[])
{
    console.log("This is question 6")
    var sum = 0;
    for(var i=0; i<arr.length; i++)
    {
        sum+=arr[i];
    }
    var avg = sum/arr.length
    return avg
}
console.log(findAverage(madeUpArr))

//====================Question 7====================\\
function arrOdd()
{
    console.log("This is question 7")
    var newArr = [];
    for(var i=0; i<=50; i++)
    {
        if(i%2!=0)
        {
            newArr.push(i);
        }
    }
    return newArr;
}
console.log(arrOdd(madeUpArr))

//====================Question 8====================\\
function greaterY(arr=[], y)
{
    console.log("This is question 8")
    var count = 0;
    for(var i =0; i<arr.length; i++)
    {
        if(arr[i]>y)
        {
            count++;
        }
    }
    return count;
}
console.log(greaterY(madeUpArr, 2));

//====================Question 9====================\\
function squares(arr=[])
{
    console.log("This is question 9")
    var newArr = [];
    for(var i=0; i<arr.length; i++)
    {
        newArr.push(arr[i]*arr[i]);
    }
    return newArr;
}
console.log(squares(madeUpArr))

//====================Question 10====================\\

var testerArr =[-1,-2,-3,-4,-5,-6,-6,-6,-7,-7,-8]
function negatives(arr=[])
{
    console.log("This is question 10")
    for(var i=0; i<arr.length; i++)
    {
        if(arr[i]<0)
        {
            arr[i] = 0;
        }
    }
    return arr;
}
console.log(negatives(testerArr))
//====================Question 11====================\\
function minMax(arr=[])
{
    console.log("This is question 11")
    var newArr =[]
    var min = arr[0];
    var max = arr[0];
    var sum = 0;
    var avg = 0;
    for(var i = 0; i<arr.length; i++)
    {
        if(arr[i]>max)
        {
            max = arr[i]
        }
        else if(arr[i]<min)
        {
            min = arr[i]
        }
        sum+=arr[i]   
    }
    avg = sum/arr.length
    newArr.push(max, min, avg)
    return newArr
}
console.log(minMax(madeUpArr))

//====================Question 12====================\\
function swapValues(arr=[])
{
    console.log("This is question 12");
    var temp=arr[0];
    arr[0] = arr[arr.length-1];
    arr[arr.length-1] =temp;
    return arr;
}
console.log(swapValues(madeUpArr))

//====================Question 13====================\\
var superTestyArr=[10, -23, 99, 202020, -9999]
function numToString(arr=[])
{
    console.log('This is question 13')
    for(var i=0; i<arr.length;i++)
    {
        if(arr[i]<0)
        {
            arr[i] = 'Dojo';
        }
    }
    return arr
}
console.log(numToString(superTestyArr));