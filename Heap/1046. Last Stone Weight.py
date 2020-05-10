"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1046. Last Stone Weight
"""

from heapq import heapify, heappop, heappush
class Solution:

    def lastStoneWeight(self, stones):
        max_heap = [-stone for stone in stones]
        heapify(max_heap)
        while len(max_heap) > 1:
            heavy_stone, light_stone = -1 * heappop(max_heap), -1 * heappop(max_heap)
            if heavy_stone != light_stone:
                remaining_stone = heavy_stone - light_stone
                heappush(max_heap, -1 * remaining_stone)
        last_stone = 0 if len(max_heap) == 0 else -1 * max_heap[0]
        return last_stone