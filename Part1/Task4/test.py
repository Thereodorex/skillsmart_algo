import unittest
from Stack import Stack, check_bracers, postfix_calc

class TestArray(unittest.TestCase):

    def test_all(self):
        stack = Stack()
        cases = [i for i in range(10)]
        for i, case in enumerate(cases):
            with self.subTest(case=case):
                stack.push(case)
                self.assertEqual(stack.size(), i + 1)
                self.assertEqual(stack.peek(), case)

        size = stack.size()
        for i, case in enumerate(cases):
            with self.subTest(case=case):
                peek = stack.peek()
                pop = stack.pop()
                self.assertEqual(stack.size(), size - i - 1)
                self.assertEqual(peek, pop)

    def test_bracers(self):
        cases = [
            '()',
            '()()',
            '(())',
            '(())()',
            '(()((())()))',
            '(()()(()',
            '())',
            ')('
            '))((',
            '((())',
        ]
        results = [
            True, True, True, True, True,
            False, False, False, False, False,
        ]

        for i, c in enumerate(cases):
            with self.subTest(case=c):
                self.assertEqual(check_bracers(c), results[i])

    def test_calc(self):
        cases = [
            '1 2 + 3 * =',
            '8 2 + 5 * 9 + =',
        ]
        results = [
            '9', '59'
        ]

        for i, c in enumerate(cases):
            with self.subTest(case=c):
                self.assertEqual(postfix_calc(c), results[i])

if __name__ == '__main__':
    unittest.main()
