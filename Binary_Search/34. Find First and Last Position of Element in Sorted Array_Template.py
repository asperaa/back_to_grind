"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""34. Find First and Last Position of Element in Sorted Array [Template]
"""

class Solution:
    def find_left_boundry(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        return -1
                
    
    def find_right_boundry(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        return left - 1


    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        left_b = self.find_left_boundry(nums, target)
        if left_b == -1:
            return [-1, -1]
        right_b = self.find_right_boundry(nums, target)
        return [left_b, right_b]