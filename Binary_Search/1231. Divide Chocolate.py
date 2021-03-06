"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1231. Divide Chocolate
"""

class Solution:

    def is_valid(self, nums, m, min_sum):
        sub_array_sum = 0
        num_of_subarray = 1
        for i in range(len(nums)):
            sub_array_sum += nums[i]
            if sub_array_sum > min_sum:
                num_of_subarray += 1
                sub_array_sum = 0
            if num_of_subarray > m:
                return False
        return True

    def maximizeSweetness(self, nums, m):
        if len(nums) < m:
            return -1
        left = min(nums)
        right = sum(nums)
        min_sum = right
        while left <= right:
            potential_min_sum = left + (right - left) // 2
            if self.is_valid(nums, m+1, potential_min_sum):
                min_sum = potential_min_sum
                right = potential_min_sum - 1
            else:
                left = potential_min_sum + 1
        return min_sum 