var users = [{name: "Michael", age:37}, {name:"John", age:30}, {name:"David", age:27}];

// Printing John's Age
console.log(users[1].age);

// Printing The Name of the First Object
console.log(users[0].name);

// Printing the Name of Each User Using a For Loop
for(var user in users)
{
    console.log(users[user].name + " - " + users[user].age)
}

