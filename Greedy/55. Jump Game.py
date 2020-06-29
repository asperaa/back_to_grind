"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""55. Jump Game
"""

class Solution:
    
    def canJump(self, nums):
        n = len(nums)
        reach = 0
        for i in range(0, n):
            if reach < i:
                return False
            reach = max(reach, i + nums[i])
        return True            