import unittest
from PowerSet import PowerSet
import string
from random import choice


class TestNativeArray(unittest.TestCase):

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

    def get_values(self, s):
        return set(s.values)

    def test_put(self):
        s = PowerSet()
        for i, k in enumerate(self.keys):
            s.put(k)
            with self.subTest(case=k):
                self.assertEqual(s.size(), i + 1)
        for k in self.keys:
            with self.subTest(case=k):
                self.assertTrue(k in s.values)

    def test_not_put(self):
        s = PowerSet()
        test = 'test string'
        s.put(test)
        self.assertEqual(s.size(), 1)
        s.put(test)
        self.assertEqual(s.size(), 1)

    def test_remove(self):
        s = PowerSet()
        test = 'test string'
        test2 = 'tst2'
        s.put(test)
        self.assertTrue(s.remove(test))
        self.assertFalse(s.remove(test))
        self.assertFalse(s.remove(test2))

    def test_intersect(self):
        s1 = PowerSet()
        s1.put('1')
        s1.put('2')
        s1.put('3')
        s2 = PowerSet()
        s2.put('3')
        s2.put('4')
        self.assertEqual(self.get_values(s1.intersection(s2)), set('3'))

    def test_intersect_empty(self):
        s1 = PowerSet()
        s1.put('1')
        s1.put('2')
        s1.put('3')
        s2 = PowerSet()
        s2.put('5')
        s2.put('4')
        self.assertEqual(self.get_values(s1.intersection(s2)), set())

    def test_union(self):
        s1 = PowerSet()
        s1.put('1')
        s1.put('2')
        s1.put('3')
        s2 = PowerSet()
        s2.put('4')
        s2.put('5')
        self.assertEqual(self.get_values(s1.union(s2)), set(['1', '2', '3', '4', '5']))

    def test_union_empty(self):
        s1 = PowerSet()
        s1.put('1')
        s1.put('2')
        s1.put('3')
        s2 = PowerSet()
        self.assertEqual(self.get_values(s1.union(s2)), set(['1', '2', '3']))

    def test_diff(self):
        s1 = PowerSet()
        s1.put('1')
        s1.put('2')
        s1.put('3')
        s2 = PowerSet()
        s2.put('1')
        s2.put('2')
        self.assertEqual(self.get_values(s1.difference(s2)), set(['3']))

    def test_diff_empty(self):
        s1 = PowerSet()
        s1.put('1')
        s1.put('2')
        s1.put('3')
        s2 = PowerSet()
        s2.put('1')
        s2.put('2')
        s2.put('3')
        self.assertEqual(self.get_values(s1.difference(s2)), set())

    def test_subset1(self):
        s1 = PowerSet()
        s1.put('1')
        s1.put('2')
        s1.put('3')
        s1.put('4')
        s2 = PowerSet()
        s2.put('1')
        s2.put('2')
        s2.put('3')
        self.assertTrue(s1.issubset(s2))
        self.assertFalse(s2.issubset(s1))

    def test_subset2(self):
        s1 = PowerSet()
        s1.put('1')
        s1.put('2')
        s1.put('3')
        s1.put('4')
        s2 = PowerSet()
        s2.put('0')
        s2.put('1')
        s2.put('2')
        s2.put('3')
        self.assertFalse(s1.issubset(s2))

    def test10k(self):
        real_set = set()
        my_set = PowerSet()
        for i in range(10000):
            val = ''.join(choice(string.ascii_uppercase) for i in range(10))
            real_set.add(val)
            my_set.put(val)
            with self.subTest(case=val):
                self.assertEqual(self.get_values(my_set), real_set)

if __name__ == '__main__':
    unittest.main()