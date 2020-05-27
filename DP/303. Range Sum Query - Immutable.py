"""We are the captains of our ships, and westay 'till the end. We see our stories through.
"""

"""303. Range Sum Query - Immutable
"""

class NumArray:
    
    def __init__(self, nums: List[int]):
        self.dp = [0 for _ in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            self.dp[i] = self.dp[i-1] + nums[i-1]
        
    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]
        
