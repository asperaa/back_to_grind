"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""904. Fruit Into Baskets
"""

class Solution:

    def totalFruit(self, nums):
        freq = {}
        n = len(nums)
        ans = 0
        start = 0
        for end in range(n):
            freq[nums[end]] = freq.get(nums[end], 0) + 1
            while len(freq) > 2:
                if freq[nums[start]] == 1:
                    del freq[nums[start]]
                else:
                    freq[nums[start]] -= 1
                start += 1
            ans = max(ans, end-start+1)
        return ans
