"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""973. K Closest Points to Origin [T - O(NlogK), S - O(K)]
"""

from heapq import heappop, heapify, heappush
class Solution:

    def kClosest(self, points, K):
        max_heap = []
        for point in points:
            heappush(max_heap, (-1*(point[0]**2 + point[1]**2), point))
            if len(max_heap) > K:
                heappop(max_heap)
        closest_points = [point for distance, point in max_heap]
        return closest_points
