class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class Deque:

    '''
    Мера сложности операций addHead/removeHead и addTail/removeTail зависит от реализации.
    В данном случае очередь реализована на двусвязном списке, поэтому сложность каждой операции O(1).
    '''

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def _addAfter(self, after, item):
        node = Node(item)
        self._size += 1
        node.next = after.next
        node.prev = after
        after.next.prev = node
        after.next = node

    def addFront(self, item):
        self._addAfter(self.head, item)

    def addTail(self, item):
        self._addAfter(self.tail.prev, item)

    def _remove(self, node):
        if self._size == 0:
            return None
        self._size -= 1
        res = node.value
        node.prev.next = node.next
        node.next.prev = node.prev
        return res

    def removeFront(self):
        return self._remove(self.head.next)

    def removeTail(self):
        return self._remove(self.tail.prev)

    def size(self):
        return self._size

def is_palindrome(self, string):
    '''
    Задание 7.2
    Проверить является ли строка палиндромом
    '''
    deq = Deque()
    for symb in string:
        deq.addTail(symb)
    while deq.size() > 1:
        front = deq.removeFront()
        tail = deq.removeTail()
        if front.value != tail.value:
            return False
    return True