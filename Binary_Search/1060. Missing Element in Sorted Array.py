"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1060. Missing Element in Sorted Array [Walked through fire]
"""

class Solution:

    def missingElement(self, nums, k):
        left, right = 0, len(nums) - 1
        miss_on_left = (nums[right] - nums[left] - 1) - (right - left - 1)
        if k > miss_on_left:
            return nums[right] + k - miss_on_left
        while left != right - 1:
            mid = left + (right-left) // 2
            miss_on_left = (nums[mid] - nums[left] - 1) - (mid - left - 1)
            if miss_on_left > k:
                right = mid
            elif miss_on_left < k:
                k = k - miss_on_left
                left = mid
            else:
                return nums[left] + k
        return nums[left] + k

