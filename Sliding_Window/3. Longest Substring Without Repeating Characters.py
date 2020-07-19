"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""3. Longest Substring Without Repeating Characters
"""

class Solution:
    
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        start = 0
        max_len = 0
        curr_len = 0
        check = {}
        for end in range(n):
            if s[end] in check:
                while check[s[end]] == 1:
                    check[s[start]] -= 1
                    start += 1
            check[s[end]] = check.get(s[end], 0) + 1
            curr_len = end - start + 1
            max_len = max(curr_len, max_len)
        return max_len


