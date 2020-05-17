"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""416. Partition Equal Subset Sum [Top Down]
"""

class Solution:

    def subset_sum_helper(self, dp, arr, s, n):
        if s == 0:
            return True
        if n == 0:
            return False
        if dp[n][s]:
            return dp[n][s]
        if s >= arr[n-1]:
            dp[n][s] = self.subset_sum_helper(dp, arr, s-arr[n-1], n-1) or self.subset_sum_helper(dp, arr, s, n-1)
            return dp[n][s]
        elif s < arr[n-1]:
            dp[n][s] = self.subset_sum_helper(dp, arr, s, n-1)
            return dp[n][s]
    
    def canPartition(self, nums):
        summ = sum(nums)
        if summ % 2 == 1:
            return False
        dp = [[None for _ in range(summ // 2 + 1)] for _ in range(len(nums) + 1)]
        return self.subset_sum_helper(dp, nums, summ // 2, len(nums))
        
