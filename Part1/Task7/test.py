import unittest
from OrderedList import OrderedList, OrderedStringList
import sys
import random

class TestList(unittest.TestCase):

    def test_compare(self):
        lst = OrderedList(True)
        lst_desc = OrderedList(False)
        cases = [
            (0, 0),
            (0, 1),
            (1, 0),
        ]
        results = [
            (0, 0),
            (1, -1),
            (-1, 1),
        ]

        for i, c in enumerate(cases):
            with self.subTest(case=c):
                res = lst.compare(c[0], c[1])
                res_desc = lst_desc.compare(c[0], c[1])
                self.assertEqual(res, results[i][0])
                self.assertEqual(res_desc, results[i][1])

    def test_tail(self):
        lst = OrderedList()
        cases = [i for i in range(10)]
        results = cases.copy()
        for i, c in enumerate(cases):
            with self.subTest(case=c):
                lst.add(c)
                res = results[:i+1]
                self.assertEqual(len(res), lst.len())
                self.assertEqual([x.value for x in lst.get_all()], res)

        for i, c in enumerate(cases[::-1]):
            with self.subTest(case=c):
                lst.delete(c)
                res = results[:10-i-1]
                self.assertEqual(len(res), lst.len())
                self.assertEqual([x.value for x in lst.get_all()], res)

    def test_front(self):
        lst = OrderedList()
        cases = [i for i in range(9, -1, -1)]
        results = [i for i in range(10)]
        for i, c in enumerate(cases):
            with self.subTest(case=c):
                lst.add(c)
                res = results[len(results)-i-1:]
                self.assertEqual(len(res), lst.len())
                self.assertEqual([x.value for x in lst.get_all()], res)

        for i, c in enumerate(cases[::-1]):
            with self.subTest(case=c):
                lst.delete(c)
                res = sorted(results[i+1:])
                self.assertEqual(len(res), lst.len())
                self.assertEqual([x.value for x in lst.get_all()], res)

    def test_mixed(self):
        lst = OrderedList()
        cases = list(range(10))
        random.shuffle(cases)
        results = cases.copy()
        for i, c in enumerate(cases):
            with self.subTest(case=c):
                lst.add(c)
                res = sorted(results[:i+1])
                self.assertEqual(len(res), lst.len())
                self.assertEqual([x.value for x in lst.get_all()], res)

        results = cases.copy()
        for i, c in enumerate(cases):
            with self.subTest(case=c):
                lst.delete(c)
                results.remove(c)
                res = sorted(results)
                self.assertEqual(len(res), lst.len())
                self.assertEqual([x.value for x in lst.get_all()], res)

    def test_find(self):
        lst = OrderedList()
        cases = list(range(-1, 3))
        cases_to_find = [
            (0, 1),
            (0, 1),
            (1,),
            (0, 1, 2, -1, 3)
        ]
        results = [
            (False, False),
            (True, False),
            (True, True),
            (True, True, True, False, False)
        ]
        for i, c in enumerate(cases):
            with self.subTest(case=c):
                if i > 0:
                    lst.add(c)
                for j, v in enumerate(cases_to_find[i]):
                    res = lst.find(v)
                    diff = lst[v] if results[i][j] else None
                    self.assertEqual(res, diff)

    def test_mixed_strings(self):
        lst = OrderedList()
        cases = list(str(x) for x in range(10))
        random.shuffle(cases)
        results = cases.copy()
        for i, c in enumerate(cases):
            with self.subTest(case=c):
                lst.add(c)
                res = sorted(results[:i+1])
                self.assertEqual(len(res), lst.len())
                self.assertEqual([x.value for x in lst.get_all()], res)

        results = cases.copy()
        for i, c in enumerate(cases):
            with self.subTest(case=c):
                lst.delete(c)
                results.remove(c)
                res = sorted(results)
                self.assertEqual(len(res), lst.len())
                self.assertEqual([x.value for x in lst.get_all()], res)

if __name__ == '__main__':
    unittest.main()