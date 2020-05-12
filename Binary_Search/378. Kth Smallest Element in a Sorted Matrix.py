"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""378. Kth Smallest Element in a Sorted Matrix
"""

from heapq import heapify, heappop, heappush

class Solution:

    def kthSmallest(self, matrix, k):
        n = len(matrix)
        min_heap = [(matrix[i][0], (i, 0)) for i in range(min(k, n))]
        heapify(min_heap)
        while k:
            element, (i, j) = heappop(min_heap)
            j += 1
            if j < n:
                heappush(matrix[i][j], (i, j))
            k -= 1
        return element