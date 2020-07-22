"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""930. Binary Subarrays With Sum [Constant Space]
"""

class Solution:
    
    def numSubarraysWithSum(self, nums, k):

        def atMostk(k):
            if k < 0:
                return 0
            ans = 0
            start = 0
            for end in range(len(nums)):
                k -= nums[end]
                while k < 0:
                    k += nums[start]
                    start += 1
                ans += end - start + 1
            return ans
        return atMostk(k) - atMostk(k-1)