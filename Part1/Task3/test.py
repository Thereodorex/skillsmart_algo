import unittest
from DynArray import DynArray

class TestArray(unittest.TestCase):

    def create_array(self, lst):
        array = DynArray()
        for item in lst:
            array.append(item)
        return array

    def get_items(self, array):
        return [array[i] for i in range(array.count)]

    def test_insert(self):
        cases = [
            ([], 0, 1),
            ([i for i in range(1)], 0, 13),
            ([i for i in range(1)], 1, 13),
            ([i for i in range(3)], 1, 13),
            ([i for i in range(15)], 2, 13),
            ([i for i in range(15)], 15, 13),
            ([i for i in range(31)], 0, 13),
            ([i for i in range(31)], 15, 13),
            ([i for i in range(31)], 30, 13),
            ([i for i in range(31)], 31, 13),
        ]
        results = [
            16,
            16,
            16,
            16,
            16,
            16,
            32,
            32,
            32,
            32
        ]
        for i, c in enumerate(cases):
            with self.subTest(case=c):
                array = self.create_array(c[0])
                array.insert(c[1], c[2])
                res = c[0]
                res.insert(c[1], c[2])
                self.assertEqual(array.count, len(res))
                self.assertEqual(array.capacity, results[i])
                self.assertEqual(self.get_items(array), res)

    def test_insert_extend(self):
        cases = [
            ([i for i in range(16)], 0, 13),
            ([i for i in range(16)], 5, 13),
            ([i for i in range(16)], 15, 13),
            ([i for i in range(16)], 16, 13),
            ([i for i in range(32)], 1, 13),
            ([i for i in range(32)], 31, 13),
        ]
        results = [
            32,
            32,
            32,
            32,
            64,
            64
        ]
        for i, c in enumerate(cases):
            with self.subTest(case=c):
                array = self.create_array(c[0])
                array.insert(c[1], c[2])
                res = c[0]
                res.insert(c[1], c[2])
                self.assertEqual(array.count, len(res))
                self.assertEqual(array.capacity, results[i])
                self.assertEqual(self.get_items(array), res)

    def test_insert_invalid_index(self):
        cases = [
            ([i for i in range(0)], 1, 13),
            ([i for i in range(1)], 2, 13),
            ([i for i in range(1)], -1, 13),
            ([i for i in range(15)], 16, 13),
        ]
        for _, c in enumerate(cases):
            with self.subTest(case=c):
                array = self.create_array(c[0])
                self.assertRaises(IndexError, array.insert, c[1], c[2])

    def test_delete(self):
        cases = [
            ([i for i in range(1)], 0),
            ([i for i in range(2)], 0),
            ([i for i in range(2)], 1),
            ([i for i in range(3)], 1),
            ([i for i in range(3)], 0),
            ([i for i in range(3)], 1),
            ([i for i in range(3)], 2),
            ([i for i in range(16)], 5),
            ([i for i in range(18)], 0),
            ([i for i in range(18)], 6),
            ([i for i in range(18)], 17),
        ]
        results = [
            16, 16, 16, 16, 16, 16, 16, 16, 32, 32, 32
        ]
        for i, c in enumerate(cases):
            with self.subTest(case=c):
                array = self.create_array(c[0])
                array.delete(c[1])
                res = c[0]
                res.pop(c[1])
                self.assertEqual(array.count, len(res))
                self.assertEqual(array.capacity, results[i])
                self.assertEqual(array.capacity, len(array.array))
                self.assertEqual(self.get_items(array), res)

    def test_delete_reduce(self):
        cases = [
            ([i for i in range(17)], 0),
            ([i for i in range(17)], 6),
            ([i for i in range(17)], 16),
            ([i for i in range(33)], 0),
        ]
        results = [
            21, 21, 21, 42
        ]
        for i, c in enumerate(cases):
            with self.subTest(case=c):
                array = self.create_array(c[0])
                array.delete(c[1])
                res = c[0]
                res.pop(c[1])
                self.assertEqual(array.count, len(res))
                self.assertEqual(array.capacity, results[i])
                self.assertEqual(array.capacity, len(array.array))
                self.assertEqual(self.get_items(array), res)

    def test_long_reduce(self):
        test_list = [i for i in range(33)]
        test_array = self.create_array(test_list)
        cases = [1, 11, 7, 5]
        results = [42, 28, 18, 16]

        for i, c in enumerate(cases):
            with self.subTest(case=c):
                for _ in range(c):
                    test_array.delete(0)
                    test_list.pop(0)
                self.assertEqual(test_array.count, len(test_list))
                self.assertEqual(test_array.capacity, results[i])
                self.assertEqual(test_array.capacity, len(test_array.array))
                self.assertEqual(self.get_items(test_array), test_list)

    def test_delete_invalid_index(self):
        cases = [
            ([i for i in range(0)], 0),
            ([i for i in range(1)], 1),
            ([i for i in range(1)], 2),
            ([i for i in range(1)], -1),
            ([i for i in range(15)], 15),
        ]
        for _, c in enumerate(cases):
            with self.subTest(case=c):
                array = self.create_array(c[0])
                self.assertRaises(IndexError, array.delete, c[1])

if __name__ == '__main__':
    unittest.main()