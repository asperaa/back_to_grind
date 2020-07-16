"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""159. Longest Substring with At Most Two Distinct Characters
"""

class Solution:
    
    def lengthOfLongestSubstringTwoDistinct(self, s):
        start = 0
        freq = {}
        max_len = 0
        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            while len(freq) > 2:
                if freq[s[start]] == 1:
                    del freq[s[start]]
                else:
                    freq[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
                
