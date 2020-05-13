"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""786. K-th Smallest Prime Fraction
"""

from heapq import heapify, heappop, heappush

class Solution:

    def kthSmallestPrimeFraction(self, A, k):
        min_heap = [(A[0] / A[i], 0, i) for i in range(len(A)-1, 0, -1)]
        heapify(min_heap)
        while k and min_heap:
            _, i, j = heappop(min_heap)
            if i+1 < len(A):
                heappush(min_heap, (A[i+1] / A[j], i+1, j))
            k -= 1
        answer = [A[i], A[j]]
        return answer

