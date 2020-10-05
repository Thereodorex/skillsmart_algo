import hashlib

class PowerSet():

    def __init__(self):
        self._size = 20000
        self.values = [[] for i in range(self._size)]
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
        if value not in self.values[index]:
            self.values[index].append(value)
            self.count += 1
        # for i in range(self._size):
        #     if self.values[index] is None:
        #         self.values[index] = value
        #         self.count += 1
        #         return
        #     if self.values[index] == value:
        #         return
        #     index += self.step
        #     index %= self._size

    def get(self, value):
        index = self.hash_fun(value)
        if value in self.values[index]:
            return True
        return False

    def remove(self, value):
        index = self.hash_fun(value)
        if value in self.values[index]:
            self.values[index].remove(value)
            self.count -= 1
            return True
        return False

    def intersection(self, set2):
        newSet = PowerSet()
        for i in set2.values:
            for j in i:
                if self.get(j):
                    newSet.put(j)
        return newSet

    def union(self, set2):
        newSet = PowerSet()
        for i in self.values:
            for j in i:
                newSet.put(j)
        for i in set2.values:
            for j in i:
                newSet.put(j)
        return newSet

    def difference(self, set2):
        newSet = PowerSet()
        for i in self.values:
            for j in i:
                if not set2.get(j):
                    newSet.put(j)
        return newSet

    def issubset(self, set2):
        for i in set2.values:
            for j in i:
                if not self.get(j):
                    return False
        return True