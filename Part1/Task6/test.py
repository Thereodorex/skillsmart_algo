import unittest
from Deque import Deque

class TestQueue(unittest.TestCase):

    def test_all(self):
        deq = Deque()
        cases = [i for i in range(10)]
        for i, case in enumerate(cases):
            with self.subTest(case=case):
                deq.addFront(case)
                self.assertEqual(deq.size(), i + 1)

        size = deq.size()
        for i, case in enumerate(cases):
            with self.subTest(case=case):
                front = deq.removeTail()
                self.assertEqual(deq.size(), size - i - 1)
                self.assertEqual(front, case)

        with self.subTest(case=case):
            front = deq.removeFront()
            self.assertEqual(deq.size(), 0)
            self.assertEqual(front, None)

        with self.subTest(case=case):
            tail = deq.removeTail()
            self.assertEqual(deq.size(), 0)
            self.assertEqual(tail, None)

        for i, case in enumerate(cases):
            with self.subTest(case=case):
                deq.addTail(case)
                self.assertEqual(deq.size(), i + 1)

        size = deq.size()
        for i, case in enumerate(cases):
            with self.subTest(case=case):
                tail = deq.removeFront()
                self.assertEqual(deq.size(), size - i - 1)
                self.assertEqual(tail, case)

        with self.subTest(case=case):
            front = deq.removeFront()
            self.assertEqual(deq.size(), 0)
            self.assertEqual(front, None)

        with self.subTest(case=case):
            tail = deq.removeTail()
            self.assertEqual(deq.size(), 0)
            self.assertEqual(tail, None)

if __name__ == '__main__':
    unittest.main()