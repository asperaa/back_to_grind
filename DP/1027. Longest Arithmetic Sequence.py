"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1027. Longest Arithmetic Sequence
"""

class Solution:

    def longestArithSeqLength(self, nums):
        dp = {}
        m = len(nums)
        maxx = 2
        for i in range(m):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = count = dp.get((j, diff), 1) + 1
                maxx = max(maxx, count)
        return maxx
