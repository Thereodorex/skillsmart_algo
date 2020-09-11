class Node:

    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    '''
    Реализация стека на списке
    '''
    def __init__(self):
        self.head = None
        self._size = 0

    def size(self):
        return self._size

    def pop(self):
        '''
        Сложность O(1)
        '''
        if self._size == 0:
            return None
        self._size -= 1
        result = self.head.value
        self.head = self.head.next
        return result

    def push(self, value):
        '''
        Сложность O(1)
        '''
        self._size += 1
        node = Node(value)
        node.next = self.head
        self.head = node

    def peek(self):
        return self.head.value


class Queue:

    '''
    Очередь на стеках
    '''

    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()
        self._size = 0

    def enqueue(self, item):
        '''
        Вставить в конец
        Сложность O(1)
        '''
        self._size += 1
        self.stack_a.push(item)

    def dequeue(self):
        '''
        Взять из начала
        Сложность (амортизированная) O(1)
        '''
        if self._size == 0:
            return None
        self._size -= 1
        if not self.stack_b.size():
            while self.stack_a.head is not None:
                self.stack_b.push(self.stack_a.pop())
        return self.stack_b.pop()

    def size(self):
        return self._size