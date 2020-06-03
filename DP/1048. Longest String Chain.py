"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1048. Longest String Chain
"""

class Solution:
    
    def longestStrChain(self, words):
        dp = {}
        for w in sorted(words, key=len):
            for i in range(len(w)):
                new_length = dp.get(w[:i] + w[i+1:], 0) + 1
                dp[w] = max(new_length, dp.get(w, 0))
        return max(dp.values())