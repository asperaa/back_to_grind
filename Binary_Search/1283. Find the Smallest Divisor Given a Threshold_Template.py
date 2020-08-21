"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1283. Find the Smallest Divisor Given a Threshold [Template]
"""

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right  = 1, max(nums)
        
        def is_valid(k):
            val = sum([(num + k -1) // k for num in nums])
            return val <= threshold
        
        while left < right:
            mid = left + (right - left) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        return left