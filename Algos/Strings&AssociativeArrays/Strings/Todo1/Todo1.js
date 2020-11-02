var music =" Pl ayTha tF u nkyM usi c "

function removeBlanks(string)
{
    var splitString = string.split(' ')
    string =splitString.join('')
    return string
}

console.log(removeBlanks(music))


var code = "0s1a3y5w7h9a2t4?6!8?0"

function getDigital(string)
{
    var newString=[]
    for(var i= 0; i<string.length-1; i++)
    {
        if(Number.isInteger(Number.parseInt(string[i])))
        {
            newString.push(string[i])
        }
    }
    console.log(newString)
    string = Number.parseInt(newString.join(""))
    return string
}
console.log(getDigital(code))

var lunch = "there's no free lunch - gotta pay yer way."
var live = "Live from New York, it's Saturday Night!"

function acronym(string)
{
    var words =string.split(' ')
    console.log(words)
    var newString = ''
    for(var i=0; i<words.length; i++)
    {
        newString += words[i][0]
    }
    string = newString.toUpperCase()
    return string
}
console.log(acronym(lunch))
console.log(acronym(live))

var crazyPie = "Honey pie, you are driving me crazy"

function nonSpace(string)
{
    var count = 0
    for(var i =0; i<string.length; i++)
    {
        if(string[i]!=' ')
        {
            count++
        }
    }
    return count
}

console.log(nonSpace(crazyPie))

var stringArr = ['Harryon', 'Vincent', 'Nimajneb', 'Olivia', 'Mike', 'Rico']
var length = 7

function removeShortStrings(arr, len)
{
    for(var i =0; i<arr.length; i++)
    {
        if(arr[i].length < len)
        {
            arr.splice(i, 1)
            i--
        }
    }
    return arr
}

console.log(removeShortStrings(stringArr, length))

