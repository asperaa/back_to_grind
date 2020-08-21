"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""875. Koko Eating Bananas
"""

class Solution:
    def minEatingSpeed(self, nums: List[int], H: int) -> int:
        n = len(nums)
        left, right = 1, max(nums)
        
        def is_valid(k):
            num_hours = 0
            for i in range(n):
                num_hours += nums[i] // k
                num_hours += 0 if nums[i]%k == 0 else 1
                if num_hours > H:
                    return False
            return True
        
        while left < right:
            mid = left + (right - left) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        return left
        