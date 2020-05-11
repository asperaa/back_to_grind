"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""264. Ugly Number II
"""

from heapq import heapify, heappop, heappush
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
            if not ugly_number * 2 in hash_map:
                heappush(min_heap, ugly_number * 2)
                hash_map[ugly_number * 2] = True
            if not ugly_number * 3 in hash_map:
                heappush(min_heap, ugly_number * 3)
                hash_map[ugly_number * 3] = True
            if not ugly_number * 5 in hash_map:
                heappush(min_heap, ugly_number * 5)
                hash_map[ugly_number * 5] = True
            count += 1

