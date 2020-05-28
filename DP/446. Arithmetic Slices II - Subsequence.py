"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""446. Arithmetic Slices II - Subsequence
"""

class Solution:

    def numberOfArithmeticSlices(self, nums):
        if not nums:
            return 0
        cache = {}
        num_of_slices = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                c1 = cache.get((i, diff), 0)
                c2 = cache.get((j, diff), 0)
                num_of_slices += c2
                cache[(i, diff)] = c1 + c2 + 1
        return num_of_slices
