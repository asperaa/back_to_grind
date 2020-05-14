"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""26. Remove Duplicates from Sorted Array
"""

class Solution:

    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        first_pointer, second_pointer = 0, 1
        while second_pointer <= len(nums) - 1:
            if nums[first_pointer] == nums[second_pointer]:
                second_pointer += 1
            else:
                first_pointer += 1
                nums[first_pointer] = nums[second_pointer]
        return first_pointer + 1
        