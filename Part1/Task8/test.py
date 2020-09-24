import unittest
from HashTable import HashTable


class TestHash(unittest.TestCase):

    def test_hash(self):
        ht1 = HashTable(200, 1)
        ht2 = HashTable(10, 1)
        cases = [
            'a', 'b', 'ab'
        ]
        results = [
            97, 98, 195
        ]

        for i, c in enumerate(cases):
            with self.subTest(case=c):
                self.assertEqual(ht1.hash_fun(c), results[i])
                self.assertEqual(ht2.hash_fun(c), results[i] % 10)

    def test_put(self):
        ht = HashTable(17, 2)
        str_to_put = chr(10)
        cases = [chr(17) for i in range(18)]
        results = [(i * 2 + 10) % 17 for i in range(17)] + [None]

        for i, c in enumerate(cases):
            with self.subTest(case=c):
                res = ht.put(str_to_put)
                str_to_put += c
                self.assertEqual(res, results[i])

    def test_find(self):
        ht = HashTable(17, 2)
        str_to_put = chr(10)
        cases = []
        for i in range(18):
            cases.append(str_to_put)
            ht.put(str_to_put)
            str_to_put += chr(17)
        results = [(i * 2 + 10) % 17 for i in range(17)] + [None]

        for i, c in enumerate(cases):
            with self.subTest(case=c):
                res = ht.find(c)
                self.assertEqual(res, results[i])

if __name__ == '__main__':
    unittest.main()