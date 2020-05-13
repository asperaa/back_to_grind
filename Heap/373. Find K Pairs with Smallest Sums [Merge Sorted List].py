"""We are the captains of our ship, and we stay 'till the end. We see our stories through.
"""

"""373. Find K Pairs with Smallest Sums [Merge Sorted List Method]
"""

from heapq import heapify, heappop, heappush

class Solution:

    def kSmallestPairs(self, num1, num2, k):
        if not num1 or not num2:
            return []
        m, n = len(num1), len(num2)
        min_heap = [(num1[i]+num2[0], i, 0) for i in range(m)]
        heapify(min_heap)
        smallest_pairs = []
        while k and min_heap:
            _, i, j = heappop(min_heap)
            smallest_pairs.append((num1[i], num2[j]))
            if j + 1 < n:
                heappush(min_heap, (num1[i] + num2[j+1], i, j+1))
            k -= 1
        return smallest_pairs