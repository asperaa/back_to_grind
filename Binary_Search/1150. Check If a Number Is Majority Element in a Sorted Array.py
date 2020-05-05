"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1150. Check If a Number Is Majority Element in a Sorted Array
"""

class Solution:

    def isMajorityElement(self, nums, target):
        length = len(nums)
        left_boundry = self.get_left_boundry(nums, target)
        right_boundry = self.get_right_boundry(nums, target)
        if left_boundry == -1:
            num_targets = 0
        else:
            num_targets = right_boundry - left_boundry + 1
        return num_targets > (length/2)

    def get_left_boundry(self, nums, target):
        left, right = 0, len(nums) - 1
        left_boundry = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left_boundry = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left_boundry
    
    def get_right_boundry(self, nums, target):
        left, right = 0, len(nums) - 1
        right_boundry = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right_boundry = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right_boundry
    

