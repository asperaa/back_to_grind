


from heapq import heapify, heappush, heappop

def rope_cost(nums):
    min_heap = []
    heapify(min_heap)
    
    for num in nums:
        heappush(min_heap, num)
    
    total_cost = 0
    while len(min_heap) >= 2:
        first = heappop(min_heap)
        second = heappop(min_heap)
        cost = first + second
        total_cost += cost
        heappush(min_heap, cost)
    return total_cost