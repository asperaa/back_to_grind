


from heapq import heapify, heappop, heappush

def frequency_sort(nums):
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
    
    max_heap = []
    heapify(max_heap)
    
    for num in nums:
        heappush(max_heap, (-1*hash_map.get(num), num))
    
    freq_sorted = []
    while len(max_heap) > 0:
        (freq, num) = heappop(max_heap)
        for _ in range(-1*freq):
            freq_sorted.append(num)
    return freq_sorted