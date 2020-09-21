class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc = True):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.__ascending = asc
        self._size = 0

    def __getitem__(self, index):
        if index + 1 > self.len():
            raise IndexError
        current = self.head.next
        for i in range(index):
            current = current.next
        return current

    def compare(self, v1, v2):
        if v1 is None or v2 is None:
            return None
        v = -1 if self.__ascending else 1
        if v1 < v2:
            return -v
        elif v2 < v1:
            return v
        else:
            return 0

    def add(self, value):
        node = Node(value)
        current = self.head.next
        while current.value is not None:
            if self.compare(value, current.value) == 1:
                break
            current = current.next
        node.prev = current.prev
        node.next = current
        current.prev.next = node
        current.prev = node
        self._size += 1

    def find(self, val):
        current = self.head.next
        while current.value is not None:
            if self.compare(val, current.value) != -1:
                break
            current = current.next
        if current.value != val:
            return None
        return current # здесь будет ваш код

    def delete(self, val):
        if self.len() == 0:
            return
        current = self.head.next
        while self.compare(val, current.value) == -1:
            current = current.next
        current.prev.next = current.next
        if current.value is None:
            return
        current.next.prev = current.prev
        self._size -= 1

    def clean(self, asc):
        self.__ascending = asc
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        return self._size

    def get_all(self):
        r = []
        node = self.head.next
        while node.value != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        return super().compare(v1, v2)