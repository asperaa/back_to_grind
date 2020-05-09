"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1283. Find the Smallest Divisor Given a Threshold
"""

class Solution:

    def is_valid(self, nums, threshold, divisor):
        sum_of_quotients = 0
        for i in range(nums):
            sum_of_quotients += (nums[i] + (divisor - 1)) // divisor
            if sum_of_quotients > threshold:
                return False
        return True
    
    def smallestDivisor(self, nums, threshold):
        left, right = 1, max(nums)
        smallest_divisor = right
        while left <= right:
            mid = left + (right - left) // 2
            if self.is_valid(nums, threshold, mid):
                smallest_divisor = mid
                right = mid - 1
            else:
                left = mid + 1
        return smallest_divisor

