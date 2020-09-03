class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable
    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i]):
                return iterable[i]
    def filter(self, iterable, callback):
        for i in range(len(iterable)-1, -1, -1):
            if not callback(iterable[i]):
                iterable.pop(i)
        return iterable
    def reject(self, iterable, callback):
        for i in range(len(iterable)-1,-1,-1):
            if callback(iterable[i]):
                iterable.pop(i)
        return iterable



_ = Underscore()
print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]