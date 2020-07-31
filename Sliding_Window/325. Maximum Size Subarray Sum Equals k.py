"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""325. Maximum Size Subarray Sum Equals k
"""

class Solution:

    def maxSubArrayLen(self, nums, k):
        ans = 0
        pre_summ = {0: -1}
        n = len(nums)
        curr_summ = 0
        for end in range(n):
            curr_summ += nums[end]
            if not curr_summ in pre_summ:
                pre_summ[curr_summ] = end
            if curr_summ - k in pre_summ:
                ans = max(ans, pre_summ[curr_summ-k])
        return ans
            
        