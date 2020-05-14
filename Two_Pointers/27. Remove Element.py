"""we are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""27. Remove Element
"""

class Solution:
    
    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[end] == val:
                end -= 1
            elif nums[start] == val:
                temp = nums[end]
                nums[end] = nums[start]
                nums[start] = temp
                end -= 1
            else:
                start += 1
        return start
