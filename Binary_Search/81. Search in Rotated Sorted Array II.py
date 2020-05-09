"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""81. Search in Rotated Sorted Array II
"""

class Solution:

    def findMinIndex(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[right] > nums[mid]: # right half is sorted.
                right = mid
            elif nums[right] == nums[mid]: # right half is totally filled with duplicate element 'X'.
                right = mid
            else: # left half is sorted.
                left = mid + 1
        return left
    
    def search_helper(self, nums, target, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
    
    def search(self, nums, target):
        min_index = self.findMinIndex(nums)
        left_part_of_pivot = self.search_helper(nums, target, 0, min_index - 1)
        right_part_of_pivot = self.search_helper(nums, target, min_index, len(nums)-1)
        return left_part_of_pivot or right_part_of_pivot

