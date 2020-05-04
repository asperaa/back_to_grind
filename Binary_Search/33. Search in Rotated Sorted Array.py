"""We are hte captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""33. Search in Rotated Sorted Array
"""

class Solution:

    def search(self, nums, target):
        min_index = self.findMinIndex(nums)
        first_half = self.binary_search(nums, 0, min_index -1, target)
        second_half = self.binary_search(nums, min_index, len(nums)-1, target)
        return max(first_half, second_half)

    def binary_search(self, nums, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return - 1

    def findMinIndex(self, nums):
        left, right = 0, len(nums) - 1 
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return left