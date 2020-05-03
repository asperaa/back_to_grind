"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""34. Find First and Last Position of Element in Sorted Array
"""


class Solution:

    def find_left_boundry(self, nums, target):
        left, right = 0, len(nums) - 1
        left_boundry = -1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                left_boundry = mid
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left_boundry
    
    def find_right_boundry(self, nums, target):
        left, right = 0, len(nums) - 1
        right_boundry = -1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                right_boundry = mid
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return right_boundry

    def searchRange(self, nums, target):
        left_boundary = self.find_left_boundry(nums, target)
        right_boundry = self.find_right_boundry(nums, target)
        return [left_boundary, right_boundry]