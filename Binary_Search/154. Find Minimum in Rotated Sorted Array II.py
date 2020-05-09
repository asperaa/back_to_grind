"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""154. Find Minimum in Rotated Sorted Array II
"""

class Solution:
    # Handle Case - [1 1 1 1 0 1 1 1 1 1 1] 
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[right] > nums[mid]:
                right = mid
            elif nums[right] == nums[mid]:
                right = mid
            else:
                left = mid + 1
        return nums[left]