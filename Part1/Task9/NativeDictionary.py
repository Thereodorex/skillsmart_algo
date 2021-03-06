class HashTable:
    '''
    Создаёт хэш-таблицу. Значения, которые можно хранить - строки.
    Индекс в массиве для строки определяется хэш-функцией с последующим
    линейным разрешением.
    '''
    def __init__(self, sz, stp):
        '''
        Предполагается, что size и step продуманы вне этого класса.
        '''
        self.size = sz if sz > 0 else 1
        self.step = stp if stp > 0 else 1
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # В качестве хэша используется сумма аски кодов символов строки (это не хорошо)
        value = str(value)
        return sum(map(ord, value)) % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[index] is None:
                return index
            index += self.step
            index %= self.size
        return None

    def put(self, value):
        '''
        Записывает значение по хэш-функции.
        Возвращает индекс слота или None.
        '''
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        return index

    def find(self, value):
        '''
        Находит индекс слота со значением или None.
        '''
        index = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[index] is None:
                return None
            if self.slots[index] == value:
                return index
            index += self.step
            index %= self.size
        return None

class NativeDictionary(HashTable):
    '''
    Реализуем словарь на основе хэш-таблицы.
    '''
    def __init__(self, sz):
        super().__init__(sz, 7)
        self.values = [None] * sz

    def is_key(self, key):
        '''
        Проверяем есть ли ключ в словаре.
        '''
        if self.find(key) is None:
            return False
        return True

    def put(self, key, value):
        '''
        Гарантированно записываем значение value по ключу key.
        '''
        index = self.find(key)
        if index is None:
            index = self.seek_slot(key)
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        '''
        Возвращает value для key или None если ключ не найден.
        '''
        index = self.find(key)
        return None if index is None else self.values[index]