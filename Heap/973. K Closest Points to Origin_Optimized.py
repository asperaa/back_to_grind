"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""973. K Closest Points to Origin [T - O(KlogN), S - O(K)]
"""

from heapq import heapify, heappop

class Solution:

    def kClosest(self, points, K):
        min_heap = [((point[0]**2 + point[1]**2), point) for point in points]
        heapify(min_heap)
        closest_points = []
        while K:
            closest_points.append(heappop(min_heap)[1])
            K -= 1
        return closest_points