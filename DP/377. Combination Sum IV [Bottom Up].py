"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""377. Combination Sum IV [Bottom Up]
"""

class Solution:

    def combinationSum4(self, nums, target):
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]