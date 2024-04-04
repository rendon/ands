import unittest

from builtin import PriorityQueue

class BuiltinTest(unittest.TestCase):
    def test_empty(self):
        pq = PriorityQueue()
        self.assertTrue(pq.empty())
        pq.push(2, [1, 2])
        self.assertFalse(pq.empty())

    def test_top(self):
        pq = PriorityQueue()
        pq.push(3, 'abc')
        pq.push(2, 'bb')
        self.assertEqual(pq.top(), (2, 'bb'))

    def test_pop(self):
        pq = PriorityQueue()
        for i in range(10, 0, -1):
            p = i - 1
            pq.push(p, 2 * p)

        actual = []
        while not pq.empty():
            top = pq.top()
            actual.append(pq.pop())

        expected = [(i, 2 * i) for i in range(10)]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
