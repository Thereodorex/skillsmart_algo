class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        # self.prev = None

class Queue:

    '''
    Очередь на закольцованном списке
    '''

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, item):
        '''
        Вставить в конец
        Сложность O(1)
        '''
        node = Node(item)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        node.next = self.head
        self.tail = node
        self._size += 1

    def dequeue(self):
        '''
        Взять из начала
        Сложность O(1)
        '''
        if self._size == 0:
            return None
        result = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self._size -= 1
        return result

    def wheel(self, count):
        if self.head is not None:
            for _ in range(count):
                self.head = self.head.next

    def size(self):
        return self._size
