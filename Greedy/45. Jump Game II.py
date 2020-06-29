"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""45. Jump Game II
"""

class Solution:
    def jump(self, nums: List[int]):
        n = len(nums)
        reach = 0
        curr_end = 0
        jump = 0
        for i in range(n-1):
            reach = max(reach, i + nums[i])
            if i == curr_end:
                jump += 1
                curr_end = reach
        return jump
        