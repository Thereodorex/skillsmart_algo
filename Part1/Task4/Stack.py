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


def check_bracers(string):
    '''
    Функция проверки сбалансированности скобок
    '''
    stack = Stack()
    for symb in string:
        if symb == '(':
            stack.push(symb)
        elif symb == ')':
            if stack.pop() != '(':
                return False
        else:
            return False
    return stack.size() == 0

def postfix_calc(string):
    '''
    Бонусное задание.
    Расчёт выражений в постфиксной записи.
    В задании не сказано, какие операции реализовать, а в примере только
    сложение и умножение, поэтому ограничусь ими.
    '''
    a = Stack()
    b = Stack()
    for token in string.split(' ')[::-1]:
        a.push(token)
    symb = a.pop()
    while symb is not None:
        if symb.isdigit():
            b.push(int(symb))
        elif symb == '+':
            b.push(b.pop() + b.pop())
        elif symb == '*':
            b.push(b.pop() * b.pop())
        elif symb == '=':
            return str(b.pop())
        symb = a.pop()
