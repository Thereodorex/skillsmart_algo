class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc = True):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self._size = 0

    def __getitem__(self, index):
        if index + 1 > self.len():
            raise IndexError
        current = self.head
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
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            current = self.head
            while current is not None:
                if self.compare(value, current.value) == 1:
                    break
                current = current.next
            if current is None:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            else:
                node.prev = current.prev
                node.next = current
                if current == self.head:
                    self.head = node
                else:
                    current.prev.next = node
                current.prev = node
        self._size += 1

    def find(self, val):
        current = self.head
        while current is not None:
            if self.compare(val, current.value) != -1:
                break
            current = current.next
        if current is None or current.value != val:
            return None
        return current

    def delete(self, val):
        if self.len() == 0:
            return
        current = self.head
        while self.compare(val, current.value) == -1:
            current = current.next
        if current is None:
            return
        if self.len() == 1:
            self.head = None
            self.tail = None
        elif current == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        elif current == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        self._size -= 1

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None
        self._size = 0

    def len(self):
        return self._size

    def get_all(self):
        r = []
        node = self.head
        while node != None:
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