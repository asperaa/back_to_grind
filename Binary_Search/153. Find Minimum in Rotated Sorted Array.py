"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""153. Find Minimum in Rotated Sorted Array
"""

class Solution:

    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left] # can do nums[right] as well because left and right are converging.