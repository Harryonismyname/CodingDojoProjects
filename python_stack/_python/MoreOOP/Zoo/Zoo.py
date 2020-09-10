class Animal:
    def __init__(self, name):
        self.name = name
        self.species = None
        self.age = 0
        self.health = 100
        self.happiness = 100
        self.maxHealth = self.health

    def display_info(self):
        print("{}".format(self.name).center(50, "="))
        print("Species:".ljust(25)+"{}".format(self.species).rjust(25))
        print("Age:".ljust(25)+"{}".format(self.age).rjust(25))
        print("Health:".ljust(25)+"{}".format(self.health).rjust(25))
        print("Happiness:".ljust(25)+"{}".format(self.happiness).rjust(25))
        return self

    def get_hungry(self):
        self.health -=5
        self.happiness -=5
        return self
    
    def feed(self):
        print("Feeding Time!".center(50, "#"))
        print("Health +10".center(50))
        print("Happiness +10".center(50))
        self.happiness+=10
        self.health+=10
        if self.health >= self.maxHealth:
            self.health = self.maxHealth
        self.display_info()
        return self



class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Lion"
        self.happiness = 75
        self.health = 125
        self.maxHealth = self.health

    def display_info(self):
        if self.happiness > 200:
            self.purr()
        return super().display_info()

    def purr(self):
        print("Prr...")

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Monkey"
        self.happiness = 150
        self.health = 75
        self.maxHealth = self.health
    
    def display_info(self):
        if self.happiness < 100:
            self.scream()
        return super().display_info()

    def scream(self):
        print("HOO! HOO! AH! HAH! AH! HAH! AH! HAH!")

class Camel(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.species = "Camel"
        self.happiness = 200
        self.health = 200
        self.maxHealth = self.health

    def display_info(self):
        if self.health < self.maxHealth/2:
            self.groan()
        return super().display_info()

    def groan(self):
        print("UGH.........")


class Zoo:
    def __init__(self, zooName):
        self.animals = {}
        self.name = zooName

    def add_animal(self, animal):
        print("Congradulations On Adopting a Brand New {}".format(animal.species).center(50))
        print("I'm sure {} is going to love it here!".format(animal.name).center(50))
        self.animals[animal.name] = animal
        return self

    def print_all_info(self):
        print("Welcome To {} Zoo!".format(self.name).center(50, "-"))
        for i in self.animals:
            self.animals[i].display_info()
        return self

def day_cycle(zoo):
    time = 0
    day_length = 24
    while (time<day_length):
        for i in zoo.animals:
            zoo.animals[i].get_hungry()
        dailyInteraction = input("What would you like to do today?\n>")
        if dailyInteraction.strip(" ").lower() =="feed":
            print("Which animal would you like to feed?\n>")
            for x in zoo.animals:
                zoo.animals[x].display_info()
            selection = input(">")
            if selection.strip(" ").lower() =="none" or selection.strip(" ").lower() =="back" or selection.strip(" ").lower() =="cancle":
                pass
            elif selection.strip(" ") in zoo.animals:
                zoo.animals[selection.strip(" ")].feed()
                pass
            elif selection.strip(" ").lower() == "exit":
                break
            else:
                pass
        elif dailyInteraction.lower().strip(" ") == "exit":
            break
        time +=1
        print("A new hour has arrived!".center(50, "^"))
        
harrys = Zoo("Harry's")
harrys.add_animal(Lion("Vincent")).add_animal(Monkey("Nimajneb")).add_animal(Camel("Mike")).print_all_info()
day_cycle(harrys)
