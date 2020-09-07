class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        item.next = None
        item.prev = None
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        res = []
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node == self.head:
                    self.head = self.head.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif node == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        res = 0
        node = self.head
        while node is not None:
            res += 1
            node = node.next
        return res

    def insert(self, afterNode, newNode):
        newNode.next = None
        newNode.prev = None
        if afterNode is None:
            # TODO Узнать почему добавляем в конец
            self.add_in_tail(newNode)
        else:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            afterNode.next = newNode
            if newNode.next:
                newNode.next.prev = newNode
            else:
                self.tail = newNode

    def add_in_head(self, newNode):
        newNode.next = self.head
        newNode.prev = None
        if self.head == None:
            self.tail = newNode
        else:
            self.head.prev = newNode
        self.head = newNode
