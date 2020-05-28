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
            for j in range(i-1, -1, -1):
                if diff[i] == diff[j]:
                    dp[i] += 1
                else:
                    break
        return sum(dp)
    
class Solution2:
    
    def numberOfArithmeticSlices(self, nums):
        curr = summ = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr += 1
                summ += curr
            else:
                curr = 0
        return summ
