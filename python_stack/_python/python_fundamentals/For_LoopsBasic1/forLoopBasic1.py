#====================Basic====================#
def basic():
    for x in range(151):
        print(x)

basic()

#====================Multiples_of_Five====================#
def multilpesOfFive():
    for x in range(5, 1005, 5):
        print(x)

multilpesOfFive()

#====================Counting,_the_Dojo_Way====================#
def countingTheDojoWay():
    for x in range(1, 101):
        if(x%10==0):
            print("Coding Dojo")
        elif(x%5 == 0):
            print("Coding")
        else:
            print(x)

countingTheDojoWay()
#====================Whoa._That_Sucker's_Huge====================#
def whoaThatSuckersHuge():
    total = 0
    for x in range(500001):
        if(x%2!=0):
            total+=x
    print(total)

whoaThatSuckersHuge()

#====================Countdown_by_Fours====================#
def countdownByFours():
    for x in range(2018, 0, -4):
        print(x)

countdownByFours()

#====================Flexible_Counter====================#

def flexibleCounter(lowNum, highNum, mult):
    for x in range(lowNum, highNum+1):
        if(x%mult==0):
            print(x)

flexibleCounter(2,9,3)