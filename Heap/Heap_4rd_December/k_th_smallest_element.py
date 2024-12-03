
from heapq import heapify, heappop, heappush

def kth_smallest(nums, k):
    max_heap = []
    heapify(max_heap)
    
    for num in nums:
        heappush(max_heap, -1 * num)
        if len(max_heap) > k:
            heappop(max_heap)
    return max_heap[0] * -1
    
    
    