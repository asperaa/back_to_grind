"""We are the capatains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1386. Cinema Seat Allocation [Linear]
"""

from collections import defaultdict

class Solution:

    def maxNumberOfFamilies(self, n, seats):
        hash_map = defaultdict(set)
        for i, j in seats:
            if j in [2, 3, 4, 5]:
                hash_map[i].add(0)
            if j in [4, 5, 6, 7]:
                hash_map[i].add(1)
            if j in [6, 7, 8, 9]:
                hash_map[i].add(2)
        ans = n * 2
        for i in hash_map:
            if len(hash_map[i]) == 3:
                ans -= 2
            else:
                ans -= 1
        return ans
