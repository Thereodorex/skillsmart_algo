import unittest
from NativeDictionary import NativeDictionary


class TestNativeArray(unittest.TestCase):

    size = 10
    keys = [
        'kot',
        'kat',
        'kaa',
        'kab',
        'kac',
        'bnmgdhfj',
        'ertyhdf',
        'fghkj',
        'dfgh',
        'werhnvf',
    ]

    def test_put(self):
        arr = NativeDictionary(self.size)

        for i, c in enumerate(self.keys):
            with self.subTest(case=c):
                for j, v in enumerate(self.keys):
                    res = True if j < i else False
                    self.assertEqual(arr.is_key(v), res)
                arr.put(c, i)
                self.assertEqual(arr.is_key(c), True)

    def test_get(self):
        arr = NativeDictionary(self.size)
        for i, c in enumerate(self.keys):
            with self.subTest(case=c):
                for j, v in enumerate(self.keys):
                    res = j if j < i else None
                    self.assertEqual(arr.get(v), res)
                arr.put(c, i)
                self.assertEqual(arr.get(c), i)

if __name__ == '__main__':
    unittest.main()