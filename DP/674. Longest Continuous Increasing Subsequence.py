"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""674. Longest Continuous Increasing Subsequence
"""

class Solution:

    def findLengthOfLCIS(self, nums):
        maxx = curr_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_len += 1
            else:
                curr_len = 1
            maxx = max(maxx, curr_len)
        return maxx 
