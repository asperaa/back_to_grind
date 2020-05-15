"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""295. Find Median from Data Stream [T - O(logn), S - O(n)]
"""

from heapq import heapify, heappush, heappop

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            if len(self.max_heap) == 0:
                heappush(self.max_heap, -1 * num)
            elif num < self.min_heap[0]:
                heappush(self.max_heap, -1 * num)
            else:
                pop_element = heappop(self.min_heap)
                heappush(self.max_heap, -1 * pop_element)
                heappush(self.min_heap, num)
        else:
            if num > -1 * self.max_heap[0]:
                heappush(self.min_heap, num)
            else:
                pop_element = -1 * heappop(self.max_heap)
                heappush(self.min_heap, pop_element)
                heappush(self.max_heap, -1 * num)
        

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-1 * self.max_heap[0] + self.min_heap[0]) * 0.5
        else:
            return -1 * self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()