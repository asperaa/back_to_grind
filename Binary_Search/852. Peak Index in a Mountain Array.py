"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""852. Peak Index in a Mountain Array
"""

class Solution:

    def peakIndexInMountainArray(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
                