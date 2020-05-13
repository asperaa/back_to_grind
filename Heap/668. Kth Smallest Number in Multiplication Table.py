"""We are the captains of pur ships, and we stay 'till the en. We see our stories through.
"""

"""668. Kth Smallest Number in Multiplication Table [Merge Sorted List Method]
"""

from heapq import heapify, heappop, heappush

class Solution:

    def findKthNumber(self, m, n, k):
        min_heap = [(i * 1, i, 0) for i in range(1, m+1)]
        heapify(min_heap)
        while k and min_heap:
            kth_smallest, i, j = heappop(min_heap)
            if j + 1 <= n:
                heappush(min_heap, (i * (j+1)), i, j+1))
            k -= 1
        return kth_smallest