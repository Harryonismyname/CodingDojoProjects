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
}
var Slist = new SLL()
console.log(Slist.addFront(42))
console.log(Slist.front())
console.log(Slist.addFront(57))
console.log(Slist.front())
console.log(Slist.removeFront())
console.log(Slist.front())

