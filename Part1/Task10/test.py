import unittest
from BloomFilter import BloomFilter


class TestNativeArray(unittest.TestCase):
    bloom = BloomFilter(32)
    cases = [
        "0123456789",
        "1234567890",
        "2345678901",
        "3456789012",
        "4567890123",
        "5678901234",
        "6789012345",
        "7890123456",
        "8901234567",
        "9012345678",
    ]

    def test(self):
        for i, c in enumerate(self.cases):
            with self.subTest(case=c):
                # for j, v in enumerate(self.cases[:i]):
                #     self.assertTrue(self.bloom.is_value(v))
                # for j, v in enumerate(self.cases[i:]):
                #     self.assertFalse(self.bloom.is_value(v))
                # self.bloom.add(c)
                self.assertTrue(self.bloom.is_value(c))

if __name__ == '__main__':
    unittest.main()