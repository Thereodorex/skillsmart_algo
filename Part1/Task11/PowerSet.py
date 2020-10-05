import hashlib

class PowerSet():

    def __init__(self):
        self.values = set()
        self.count = 0

    def size(self):
        return len(self.values)

    def hash_fun(self, value):
        '''
        Для скорости использую стандартную функцию hash.
        Надо придумать свою реализацию хэш функции. 
        '''
        return hash(value) % self._size

    def put(self, value):
        if value not in self.values:
            self.values.add(value)
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
        return value in self.values

    def remove(self, value):
        if value in self.values:
            self.values.remove(value)
            return True
        return False

    def intersection(self, set2):
        newSet = PowerSet()
        values = self.values & set2.values
        newSet.values = values
        return newSet

    def union(self, set2):
        newSet = PowerSet()
        values = self.values | set2.values
        newSet.values = values
        return newSet

    def difference(self, set2):
        newSet = PowerSet()
        values = self.values - set2.values
        newSet.values = values
        return newSet

    def issubset(self, set2):
        return set2.values.issubset(self.values)