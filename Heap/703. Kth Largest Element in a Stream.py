"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""703. Kth Largest Element in a Stream
"""

from heapq import heapify, heappush, heappop

class KthLargest:
    
    def min_heapify(self, k, nums):
        min_heap = []
        heapify(min_heap)
        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)
        return min_heap
        

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.min_heap = self.min_heapify(k, nums)
        

    def add(self, val: int) -> int:
            heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heappop(self.min_heap)
            return self.min_heap[0]