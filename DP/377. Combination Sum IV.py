"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""377. Combination Sum IV [Naive]
"""

class Solution:

    def combinationSum4(self, nums, target):
        if target == 0:
            return 1
        result = 0
        for num in nums:
            if target >= num:
                result += self.combinationSum4(nums, target-num)
        return result