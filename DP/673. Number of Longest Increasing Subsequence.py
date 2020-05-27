"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

class Solution:
    def findNumberOfLIS(self, nums):
        m = len(nums)
        if not m:
            return 0
        dp = [1 for _ in range(m)]
        freq = [1 for _ in range(m)]
        maxx = 1
        for i in range(1, m):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    freq[i] = freq[j]
                    maxx = max(maxx, dp[i])
                elif nums[j] < nums[i] and dp[j] + 1 == dp[i]:
                    freq[i] += freq[j]
        return sum([freq[i] for i in range(m) if dp[i] == maxx])