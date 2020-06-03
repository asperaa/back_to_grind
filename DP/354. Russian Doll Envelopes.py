"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""354. Russian Doll Envelopes [T - O(n2)] [Walked through fire]
"""

class Solution:

    def maxEnvelopes(self, nums):
        if not nums:
            return 0
        nums = sorted(nums)
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i][0] > nums[j][0] and nums[i][1] > nums[j][1] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
                    