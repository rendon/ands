import unittest
import random

from main import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(quick_sort([]), [])

    def test_sorted(self):
        nums = [i for i in range(100)]
        expected = [i for i in range(100)]
        self.assertEqual(quick_sort(nums), expected)

    def test_unsorted(self):
        nums = [i for i in range(100)]
        random.shuffle(nums)
        expected = [i for i in range(100)]
        self.assertEqual(quick_sort(nums), expected)


if __name__ == '__main__':
    unittest.main()
