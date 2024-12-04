

from heapq import heapify, heappop, heappush

def top_k_frequent(nums, k):
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
    
    min_heap = []
    heapify(min_heap)
    
    for num in nums:
        heappush(min_heap, (hash_map.get(num), num))
        if len(min_heap) > k:
            heappop(min_heap)
    top_k = []
    while len(min_heap) > 0:
        top_k.append(heappop(min_heap))
    return top_k
        
    