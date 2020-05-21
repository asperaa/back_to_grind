"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""377. Combination Sum IV [Top Down]
"""

class Solution:

    def combinationSum4(self, nums, target):
        dp = [None for _ in range(target+1)]
        dp[0] = 0
        return self.helper(nums, target, dp)

    def helper(self, nums, target, dp):
        if dp[target]:
            return dp[target]
        res = 0
        for num in nums:
            if target >= num:
                res += self.helper(nums, target-num, dp)
        dp[target] = res
        return dp[target]