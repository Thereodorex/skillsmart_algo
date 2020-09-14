import unittest
from Queue_ll import Queue

class TestQueue(unittest.TestCase):

    def test_all(self):
        qu = Queue()
        cases = [i for i in range(10)]
        for i, case in enumerate(cases):
            with self.subTest(case=case):
                qu.enqueue(case)
                self.assertEqual(qu.size(), i + 1)

        size = qu.size()
        for i, case in enumerate(cases):
            with self.subTest(case=case):
                pop = qu.dequeue()
                self.assertEqual(qu.size(), size - i - 1)
                self.assertEqual(pop, case)

        with self.subTest(case=case):
            pop = qu.dequeue()
            self.assertEqual(qu.size(), 0)
            self.assertEqual(pop, None)

        for i, case in enumerate(cases):
            with self.subTest(case=case):
                qu.enqueue(case)
                self.assertEqual(qu.size(), i + 1)

        size = qu.size()
        for i, case in enumerate(cases):
            with self.subTest(case=case):
                pop = qu.dequeue()
                self.assertEqual(qu.size(), size - i - 1)
                self.assertEqual(pop, case)

        with self.subTest(case=case):
            pop = qu.dequeue()
            self.assertEqual(qu.size(), 0)
            self.assertEqual(pop, None)

        with self.subTest(case=case):
            pop = qu.dequeue()
            self.assertEqual(qu.size(), 0)
            self.assertEqual(pop, None)

if __name__ == '__main__':
    unittest.main()
