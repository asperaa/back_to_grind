"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""300. Longest Increasing Subsequence
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = len(nums)
        if not m:
            return 0
        dp = [1 for _ in range(m)]
        maxx = 1
        for i in range(1, m):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    maxx = max(maxx, dp[i])
        return maxx