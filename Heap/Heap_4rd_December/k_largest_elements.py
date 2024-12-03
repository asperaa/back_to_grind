from heapq import heapify, heappop, heappush

def k_largest(nums, k):
    min_heap = []
    heapify(min_heap)
    for num in nums:
        heappush(min_heap, num)
        if len(min_heap) > k:
            heappop(min_heap)
    return min_heap