"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""373. Find K Pairs with Smallest Sums
"""

from heapq import heapify, heappop, heappush

class Solution:

    def kSmallestPairs(self, num1, num2, k):
        if not num1 or not num2:
            return []
        min_heap = [(num1[0]+num2[0], 0, 0)]
        heapify(min_heap)
        visited = {(0, 0): True}
        result = []
        while k and min_heap:
            summ, index_1, index_2 = heappop(min_heap)
            result.append((num1[index_1], num2[index_2]))
            if index_1 + 1 <= len(num1) - 1 and (index_1 + 1, index_2) not in visited:
                heappush(min_heap, (num1[index_1+1]+ num2[index_2], index_1+1, index_2))
                visited[(index_1+1, index_2)] = True
            if index_2 + 1 <= len(num2) - 1 and (index_1, index_2 + 1) not in visited:
                heappush(min_heap, (num1[index_1] + num2[index_2+1], index_1, index_2+1))
                visited[(index_1, index_2+1)] = True
            k -= 1
        return result        
