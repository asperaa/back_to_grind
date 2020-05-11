"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""264. Ugly Number II
"""

from heapq import heapify, heappop, heappush
class Solution:
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hash_map = {}
        min_heap = [1]
        hash_map[1] = True
        heapify(min_heap)
        count = 1
        while True:
            ugly_number = heappop(min_heap)
            if count == n:
                return ugly_number
            for i in [2, 3, 5]:
                if not ugly_number * i in hash_map:
                    heappush(min_heap, ugly_number * i)
                    hash_map[ugly_number * i] = True
            count += 1

