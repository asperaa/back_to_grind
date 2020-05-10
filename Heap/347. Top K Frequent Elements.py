"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""347. Top K Frequent Elements
"""

from heapq import heapify, heappop, heappush

class Solution:

    def topKFrequent(self, nums, k):
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        min_heap = []
        heapify(min_heap)
        for num, freq in hash_map.items():
            heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heappop(min_heap)
        frequent_elements = [num for freq, num in min_heap]
        return frequent_elements