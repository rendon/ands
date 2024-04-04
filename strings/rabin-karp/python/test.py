import unittest

from main import find

class RabinKarpTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find("abc", ""), 0)
        self.assertEqual(find("", ""), 0)

    def test_pattern_longer_than_text(self):
        self.assertEqual(find("ab", "abcd"), -1)

    def test_match(self):
        self.assertEqual(find("hello world", "hello"), 0)
        self.assertEqual(find("hello world", "world"), 6)


if __name__ == "__main__":
    unittest.main()
