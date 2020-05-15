"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""502. IPO
"""

from heapq import heappop, heappush, heapify

class Solution:

    def findMaximizedCapital(self, k, W, profits, capital):
        projects = sorted(zip(profits, capital), key = lambda x: x[1])
        max_heap = []
        i = 0
        for _ in range(k):
            while i < len(projects) and W >= projects[i][1]:
                heappush(max_heap, -projects[i][0])
                i += 1 
            if max_heap:
                W += -1 * heappop(max_heap) 
        return W