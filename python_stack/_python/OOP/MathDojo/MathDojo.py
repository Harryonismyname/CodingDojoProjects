class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for i in nums:
            num += i
        print("\n","+"*20,"\nAdding {} to {}\n".format(num, self.result), "+"*20,"\n")
        self.result += num
        print("="*20, "\nResult:\n{}".format(self.result))
        return self


    def subtract(self, num, *nums):
        for i in nums:
            num += i
        print( "\nSubtracting {} from {}\n".format(num, self.result),"-"*20)
        self.result -= num
        print("="*20, "\nResult:\n{}\n".format(self.result))
        return self



md = MathDojo()

x = md.add(2).add(2,5,1).add(1,2,3,4,5,6,7,8,9,10).subtract(3,2).subtract(59).subtract(99999,99999,99999,99999).add(399996).result
print(x)

