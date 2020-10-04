import hashlib

class PowerSet():

    def __init__(self):
        self._size = 20000
        self.values = [None] * self._size
        self.step = 13
        self.count = 0

    def hash_fun(self, value):
        '''
        Для скорости использую стандартную функцию hash.
        Надо придумать свою реализацию хэш функции. 
        '''
        return hash(value) % self._size

    def size(self):
        return self.count

    def put(self, value):
        index = self.hash_fun(value)
        for i in range(self._size):
            if self.values[index] is None:
                self.values[index] = value
                self.count += 1
                return
            if self.values[index] == value:
                return
            index += self.step
            index %= self._size

    def get(self, value):
        index = self.hash_fun(value)
        for i in range(self._size):
            if self.values[index] == value:
                return True
            if self.values[index] is None:
                return False
            index += self.step
            index %= self._size
        return False

    def remove(self, value):
        index = self.hash_fun(value)
        for i in range(self._size):
            if self.values[index] == value:
                self.values[index] = None
                self.count -= 1
                return
            if self.values[index] is None:
                return
            index += self.step
            index %= self._size

    def intersection(self, set2):
        newSet = PowerSet()
        for i in set2.values:
            if i is not None and self.get(i):
                newSet.put(i)
        return newSet

    def union(self, set2):
        newSet = PowerSet()
        for i in self.values:
            if i is not None:
                newSet.put(i)
        for i in set2.values:
            if i is not None:
                newSet.put(i)
        return newSet

    def difference(self, set2):
        newSet = PowerSet()
        for i in self.values:
            if i is not None and not set2.get(i):
                newSet.put(i)
        return newSet

    def issubset(self, set2):
        for i in set2.values:
            if i is not None and not self.get(i):
                return False
        return True