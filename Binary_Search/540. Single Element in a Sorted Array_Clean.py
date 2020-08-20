"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""540. Single Element in a Sorted Array
"""

class Solution:

    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) // 2
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid * 2] != nums[mid*2 + 1]:
                right = mid
            else:
                left = mid + 1
        return nums[left * 2]