"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""413. Arithmetic Slices
"""

class Solution:
    
    def numberOfArithmeticSlices(self, nums):
        diff = []
        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i-1])
        dp = [0 for _ in range(len(diff))]
        for i in range(1, len(diff)):
            if diff[i] == diff[i-1]:
                    dp[i] = dp[i-1] + 1
        return sum(dp)