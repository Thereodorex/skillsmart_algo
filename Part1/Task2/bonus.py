class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    '''
    Версия класса с фиктивными началом и концом. Для корректной работы переменная value
    (не фиктивная) не должна принимать значение None.
    node.value == None обозначает выход за границы списка
    Для получения "рабочего" начала неободимо обращаться self.head.next.
    Для получения "рабочего" конца неободимо обращаться self.tail.prev.
    '''  
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        item.next = self.tail
        item.prev = self.tail.prev
        item.prev.next = item
        self.tail.prev = item

    def find(self, val):
        node = self.head.next
        while node.value is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head.next
        res = []
        while node.value is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all=False):
        node = self.head.next
        while node.value is not None:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        res = 0
        node = self.head.next
        while node.value is not None:
            res += 1
            node = node.next
        return res

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            newNode.prev = afterNode
            afterNode.next = newNode
            newNode.next.prev = newNode

    def add_in_head(self, newNode):
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next = newNode
        newNode.next.prev = newNode
