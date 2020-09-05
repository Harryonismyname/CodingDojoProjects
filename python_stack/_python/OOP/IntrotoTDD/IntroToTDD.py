import unittest

def reverseList(list):
    halfway = int(len(list)/2)
    for j in range(len(list)-1,halfway,-1):
        list.append(list[j])
        list.pop(j)
    for i in range(halfway, -1, -1):
        list.append(list[i])
        list.pop(i)
    return list


def isPalindrome(string):
    newString = ""
    for x in range(len(string)-1,-1,-1):
        newString +=string[x]
    if newString == string:
        return True
    else:
        return False

def coin(integer):
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    
    while(integer>0):
        if integer>=25:
            quarters+=1
            integer-=25
            continue
        elif integer>=10:
            dimes+=1
            integer-=10
            continue
        elif integer>=5:
            nickles+=1
            integer-=5
            continue
        else:
            pennies+=1
            integer-=1
    finalList= [quarters, dimes, nickles, pennies]
    return finalList

def factorial(num):
    val = num
    if num > 1:
        val *= factorial(num-1)
        return val
    return val

def fibonacci(f):
    
    menu = f
    if f<2:
        return 0
    if f == 2:
        return 1
    elif f>2:
        menu = fibonacci(f-1)+fibonacci(f-2)
        return menu


class TestCases(unittest.TestCase):

    def reverseTest1(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def reverseTest2(self):
        self.assertEqual(reverseList([9,8,7,6,5,4,3,2,1]),[1,2,3,4,5,6,7,8,9])
    def reverseTest3(self):
        self.assertEqual(reverseList([12,34,56,78,90]),[90,78,56,34,12])

    def palindromeTest1(self):
        self.assertTrue(isPalindrome("hannah"))
    def palindromeTest2(self):
        self.assertFalse(isPalindrome("tommy"))
    def palindromeTest3(self):
        self.assertTrue(isPalindrome("racecar"))
    def palindromeTest4(self):
        self.assertTrue(isPalindrome("racecar"))
    def palindromeTest5(self):
        self.assertFalse(isPalindrome("rabcr"))
    def palindromeTest6(self):
        self.assertTrue(isPalindrome("tacocat"))
    def palindromeTest7(self):
        self.assertFalse(isPalindrome("RUNAWAY"))

    def coinTest1(self):
        self.assertEqual(coin(87), [3,1,0,2])
    def coinTest2(self):
        self.assertNotEqual(coin(87), [4, 3, 0, 2])
    def coinTest3(self):
        self.assertNotEqual(coin(280), [9, 2, 4, 6])
    def coinTest4(self):
        self.assertEqual(coin(49), [1, 2,0,4])
    def coinTest5(self):
        self.assertNotEqual(coin(200), [1,2, 3, 4])
    def coinTest6(self):
        self.assertEqual(coin(45),[1,2,0,0])
    
    def factorialTest1(self):
        self.assertEqual(factorial(5), 120)
    def factorialTest2(self):
        self.assertEqual(factorial(11), 39916800)
    def factorialTest3(self):
        self.assertNotEqual(factorial(3), 9)
    def factorialTest4(self):
        self.assertNotEqual(factorial(7), 21)

    def fiboTest1(self):
        self.assertEqual(fibonacci(5), 3)
    def fiboTest2(self):
        self.assertEqual(fibonacci(4), 2)
    def fiboTest3(self):
        self.assertNotEqual(fibonacci(7), 13)
    def fiboTest4(self):
        self.assertNotEqual(fibonacci(20), 18)


test = TestCases()
test.reverseTest1()
test.reverseTest2()
test.reverseTest3()

test.palindromeTest1()
test.palindromeTest2()
test.palindromeTest3()
test.palindromeTest4()
test.palindromeTest5()
test.palindromeTest6()
test.palindromeTest7()

test.coinTest1()
test.coinTest2()
test.coinTest3()
test.coinTest4()
test.coinTest5()
test.coinTest6()

test.factorialTest1()
test.factorialTest2()
test.factorialTest3()
test.factorialTest4()

test.fiboTest1()
test.fiboTest2()
test.fiboTest3()
test.fiboTest4()