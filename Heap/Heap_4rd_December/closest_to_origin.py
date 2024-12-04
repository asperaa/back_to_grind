


from heapq import heapify, heappop, heappush

def k_closest(nums, k):
    max_heap = []
    heapify(max_heap)
    
    for num in nums:
        x, y = num
        heappush(max_heap, (-1 * (x**2 + y**2), num))
        
        if len(max_heap)>k:
            heappop(max_heap)
    k_closest = [num for dist, num in max_heap]
    return k_closest