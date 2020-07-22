"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""930. Binary Subarrays With Sum
"""

from collections import Counter
class Solution:

    def numSubarraysWithSum(self, nums, k):
        freq = Counter({0:1})
        curr_pre_sum = 0
        ans = 0
        for num in nums:
            curr_pre_sum += num
            if curr_pre_sum - k in freq:
                ans += freq[curr_pre_sum-k]
            freq[curr_pre_sum] += 1
        return ans