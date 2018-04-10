"""
Structs

Auxiliary structures to algorithms
"""
import heapq


class PriorityQueue:
    """
    Implements a priority queue
    """
    def __init__(self):
        self.heap = []

    def push(self, element):
        """
        Inserts an element on the queue

        Parameters
        ----------
        element: list
            With elements to put on the queue
        """
        heapq.heappush(self.heap, element)

    def pop(self):
        """
        Removes the priority element on the queue.
        In other words, removes the first inserted
        value (FIFO)
        """
        return heapq.heappop(self.heap)
