class Node
{
    constructor(value)
    {
        this.value = value
        this.next = null
    }
}

class SLL
{
    constructor()
    {
        this.head = null
    }
    validator()
    {
        if(this.head == null)
        {
            return false
        }
        else
        {
            return true
        }
    }
    addFront(value)
    {
        var newNode = new Node(value)
        newNode.next = this.head
        this.head = newNode
        return this.head
    }
    removeFront()
    {
        if(this.validator())
        {
            this.head = this.head.next
            return this.head
        }
        else
        {
            return null
        }
    }
    front()
    {
        if(this.validator())
        {
            return this.head.value
        }
        else
        {
            return null
        }
    }
    contains(value)
    {
        if(this.validator())
        {
            var runner = this.head
            while(runner.next != null)
            {
                runner = runner.next
                if (runner.value == value)
                {
                    return true
                }
            }
            return false
        }
        else
        {
            return null
        }
    }
    length()
    {
        var runner =this.head
        var count = 0
        while(runner != null)
        {
            runner= runner.next
            count++
        }
        return count
    }
    display()
    {
        if(this.validator)
        {
            var runner = this.head
            var displayString = "["
            while(runner!=null)
            {
                if(runner.next !=null)
                {
                    displayString += runner.value +", "
                }
                else if (runner.next ==null)
                {
                    displayString+= runner.value + "]"
                }
                runner=runner.next
            }
            return displayString
        }
        else
        {
            return "[]"
        }
    }
    max()
    {
        if(this.validator)
        {
            var runner =this.head
            var max = this.head.value
            while(runner !=null)
            {
                if (runner.value> max)
                {
                    max = runner.value
                }
                runner= runner.next
            }
            return max
        }
        else
        {
            return null
        }
    }
    min()
    {
        if(this.validator())
        {
            var runner= this.head
            var min = this.head.value
            while(runner != null)
            {
                if(runner.value<min)
                {
                    min= runner.value
                }
                runner = runner.next
            }
            return min
        }
        else
        {
            return null
        }
    }
    average()
    {
        if(this.validator())
        {
            var runner =this.head
            var total = 0
            var avg = 0
            while(runner != null)
            {
                avg += runner.value
                total++
                runner= runner.next
            }
            avg = avg/total
            return avg
        }
        else
        {
            return null
        }
    }
}
var Slist = new SLL()
console.log(Slist.addFront(42))
console.log(Slist.addFront(57))
console.log(Slist.addFront(1))
console.log(Slist.addFront(2))
console.log(Slist.addFront(3))
console.log(Slist.addFront(4))
console.log(Slist.addFront(5))
console.log(Slist.addFront(6))
console.log(Slist.addFront(7))
console.log(Slist.addFront(8))
console.log(Slist.addFront(9))
console.log(Slist.max())
console.log(Slist.min())
console.log(Slist.average())
