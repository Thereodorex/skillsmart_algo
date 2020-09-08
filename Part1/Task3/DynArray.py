import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        '''
        Сложность алгоритма O(n)
        '''
        if i > self.count or i < 0:
            raise IndexError('Index is out of bounds')
        old_array = self.array
        if self.count + 1 > self.capacity:
            self.capacity *= 2
            self.array = self.make_array(self.capacity)
            for index in range(0, i):
                self.array[index] = old_array[index]
        for index in range(self.count, i, -1):
            self.array[index] = old_array[index - 1]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        '''
        Сложность алгоритма 0(n)
        '''
        if i >= self.count or i < 0:
            raise IndexError('Index is out of bounds')
        old_array = self.array
        if self.count - 1 <= self.capacity // 2 and self.capacity != 16:
            self.capacity //= 2
            if self.capacity < 16:
                self.capacity = 16
            self.array = self.make_array(self.capacity)
            for index in range(0, i):
                self.array[index] = old_array[index]
        self.count -= 1
        for i in range(i, self.count):
            self.array[i] = old_array[i+1]