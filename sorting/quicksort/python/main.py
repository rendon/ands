# Reference: Algorithms 4th Ed., Robert Sedgewick, Kevin Wayne

import random
from typing import List


def quick_sort(a):
    # This step lowers the chances of running into the worst-case scenario.
    random.shuffle(a)

    qsort(a, 0, len(a))
    return a


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def qsort(a, lo, hi):
    if lo >= hi:
        return

    lt = lo      #  less-than pointer
    i = lo + 1
    gt = hi - 1  #  greater-than pointer
    v = a[lo]

    # 3-way partitioning
    while i <= gt:
        if a[i] < v:
            swap(a, lt, i)
            lt += 1
            i += 1
        elif a[i] > v:
            swap(a, i, gt)
            gt -= 1
        else:
            i += 1

    qsort(a, lo, lt)
    qsort(a, gt + 1, hi)

