"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""312. Burst Balloons
"""

class Solution:
    
    def maxCoins(self, nums):
        m = len(nums) + 2
        dp = [[None for _ in range(m+1)]for _ in range(m+1)]
        return self.helper([1] + nums + [1], 1, m-1, dp)
    
    def helper(self, nums, i, j, dp):
        if dp[i][j]:
            return dp[i][j]
        if i >= j:
            return 0
        max_cost = float('-inf')
        for k in range(i, j):
            left = self.helper(nums, i, k, dp)
            right = self.helper(nums, k+1, j, dp)
            cost = left + right + nums[i-1] * nums[k] * nums[j]
            max_cost = max(max_cost, cost)
        dp[i][j] = max_cost
        return max_cost


