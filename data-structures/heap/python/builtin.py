from heapq import heappush, heappop

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def push(self, priority, value):
        heappush(self._elements, (priority, value))

    def pop(self):
        return heappop(self._elements)

    def empty(self):
        return len(self._elements) == 0

    def top(self):
        return self._elements[0]
