"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""992. Subarrays with K Different Integers
"""

class Solution:
    
    def subarraysWithKDistinct(self, nums, k):

        def atMostK(k):
            freq = {}
            start = 0
            ans = 0
            n = len(nums)
            for end in range(n):
                freq[nums[end]] = freq.get(nums[end], 0) + 1
                while len(freq) > k:
                    freq[nums[start]] -= 1
                    if freq[nums[start]] == 0:
                        del freq[nums[start]]
                    start += 1
                ans += end - start + 1
            return ans
        return atMostK(k) - atMostK(k-1)