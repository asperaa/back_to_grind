"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""646. Maximum Length of Pair Chain
"""

class Solution:

    def findLongestChain(self, pairs):
        n = len(pairs)
        pairs = sorted(pairs)
        if n < 2:
            return n
        dp = [1 for _ in range(n)]
        maxx = float('-inf')
        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                maxx = max(maxx, dp[i])
        return maxx