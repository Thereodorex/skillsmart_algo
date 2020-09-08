class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        '''
        Сложность O(n), так как используем начало списка как верхушку стека.
        Если использовать конец списка в качестве верхушки, то будет O(1)
        '''
        if not self.stack:
            return None
        return self.stack.pop(0)

    def push(self, value):
        '''
        Сложность O(n), так как используем начало списка как верхушку стека.
        Если использовать конец списка в качестве верхушки, то будет O(1)
        '''
        self.stack.insert(0, value)

    def peek(self):
        if not self.stack:
            return None
        return self.stack[0]


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
