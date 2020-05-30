"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""213. House Robber II
"""

class Solution:

    def rob_helper(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
        return dp[n]
    
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob_helper(nums[0:n-1]), self.rob_helper(nums[1:n]))

