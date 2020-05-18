"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""494. Target Sum
"""

class Solution:
    
    def target_sum_helper(self, nums, curr_sum, n):
        if (n, curr_sum) in self.book:
            return self.book[(n, curr_sum)]
        if curr_sum == self.S and n == 0:
            return 1
        if n == 0:
            return 0
        positive = self.target_sum_helper(nums, curr_sum + nums[n-1], n-1)
        negative = self.target_sum_helper(nums, curr_sum - nums[n-1], n-1)
        self.book[(n, curr_sum)] = positive + negative
        return self.book[(n, curr_sum)]
    
    def findTargetSumWays(self, nums, S):
        self.S = S
        self.book = {}
        return self.target_sum_helper(nums, 0, len(nums))