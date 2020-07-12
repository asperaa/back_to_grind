"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1296. Divide Array in Sets of K Consecutive Numbers
"""

from collections import Counter

class Solution:

    def isPossibleDivide(self, nums, k):
        count = Counter(nums)
        keys = sorted(count)
        for i in keys:
            if count[i] > 0:
                freq = count[i]
                for j in range(i, i+k):
                    if count[j] < freq:
                        return False
                    count[j] -= freq
        return True

