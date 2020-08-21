"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1482. Minimum Number of Days to Make m Bouquets
"""

class Solution:
    def minDays(self, nums: List[int], m: int, k: int) -> int:
        left, right = 1, max(nums)
        if len(nums) < m*k:
            return -1
        
        def is_valid(days):
            num_bou = 0
            num_flowers = 0
            for bloom in nums:
                if bloom > days:
                    num_flowers = 0
                else:
                    num_flowers = num_flowers + 1
                    if num_flowers == k:
                        num_bou += 1
                        num_flowers = 0
            return num_bou >= m
        
        while left < right:
            mid = left + (right - left) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        return left
            