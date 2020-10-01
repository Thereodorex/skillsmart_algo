class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0
        self.mask1 = 0
        self.mask2 = 0
        for i in range(f_len):
            self.filter = (self.filter << 1) | 1

    def hash1(self, str1):
        res = 0
        for i, c in enumerate(str1):
            res = (res * 17 + ord(c) + i) % self.filter_len
        return 1 << res

    def hash2(self, str1):
        res = 0
        for i, c in enumerate(str1):
            res = (res * 223 + ord(c) + i) % self.filter_len
        return 1 << res

    def add(self, str1):
        self.mask1 |= self.hash1(str1)
        self.mask2 |= self.hash2(str1)

    def is_value(self, str1):
        if self.mask1 & self.hash1(str1) and \
        self.mask2 & self.hash2(str1):
            return True
        return False