"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1231. Divide Chocolate [Template]
"""

class Solution:
    def maximizeSweetness(self, nums: List[int], K: int) -> int:
        left, right = min(nums), sum(nums)
        
        def is_valid(min_sweet):
            num_partitions = 1
            curr_sweet = 0
            for sweet in nums:
                curr_sweet += sweet
                if curr_sweet > min_sweet:
                    num_partitions += 1
                    curr_sweet = 0
                if num_partitions > K+1:
                    return False
            return True
        while left < right:
            mid = left + (right - left) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        return left
        