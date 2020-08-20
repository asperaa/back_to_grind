"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1060. Missing Element in Sorted Array [Clean]
"""

class Solution:
    def missingElement(self, nums, k):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] - nums[0] - mid >= k:
                right = mid
            else:
                left = mid + 1
        return nums[0] + left - 1 + k