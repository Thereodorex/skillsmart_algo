import hashlib

class PowerSet():

    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def put(self, value):
        if value not in self.values:
            self.values.append(value)

    def get(self, value):
        if value in self.values:
            return True
        return False

    def remove(self, value):
        if value in self.values:
            self.values.remove(value)
            return True
        return False

    def intersection(self, set2):
        newSet = PowerSet()
        for i in set2.values:
            if i in self.values:
                newSet.put(i)
        return newSet

    def union(self, set2):
        newSet = PowerSet()
        for i in self.values:
            newSet.put(i)
        for i in set2.values:
            newSet.put(i)
        return newSet

    def difference(self, set2):
        newSet = PowerSet()
        for i in self.values:
            if i not in set2.values:
                newSet.put(i)
        return newSet

    def issubset(self, set2):
        for i in set2.values:
            if i not in self.values:
                return False
        return True