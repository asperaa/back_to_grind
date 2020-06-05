"""We are the captains of our ships, and we stay 'till the end. We seeour stories through.
"""

"""1039. Minimum Score Triangulation of Polygon
"""

class Solution:

    def minScoreTriangulation(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [[None for _ in range(n+1)]for _ in range(n+1)]
        return self.helper(nums, 0, n-1, dp)
    
    def helper(self, nums, i, j, dp):
        if dp[i][j]:
            return dp[i][j]
        if j - i < 2:
            return 0
        minn = float('inf')
        for k in range(i+1, j):
            left_cost = self.helper(nums, i, k, dp)
            right_cost = self.helper(nums, k, j, dp)
            total_cost = left_cost + right_cost + nums[i] * nums[k] * nums[j]
            minn = min(minn, total_cost)
        dp[i][j] = minn
        return minn
