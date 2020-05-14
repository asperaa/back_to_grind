"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""283. Move Zeroes
"""

class Solution:

    def moveZeroes(self, nums):
        if len(nums) <= 1:
            return nums
        first_pointer, second_pointer = 0, 1
        while second_pointer <= len(nums) - 1:
            if nums[first_pointer] == 0 and nums[second_pointer] == 0:
                second_pointer += 1
            elif nums[first_pointer] == 0  and nums[second_pointer] != 0:
                temp = nums[second_pointer]
                nums[second_pointer] = nums[first_pointer]
                nums[first_pointer] = temp
                first_pointer += 1
                second_pointer += 1
            else:
                first_pointer += 1
                second_pointer += 1
