"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1092. Shortest Common Supersequence
"""

class Solution:
    
    def shortestCommonSupersequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[None for _ in range(n+1)]for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for j in range(1, n+1):
            dp[0][j] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        i, j = m, n
        result = []
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                result.append(text1[i-1])
                j -= 1
                i -= 1
            else:
                if dp[i-1][j] >= dp[i][j-1]:
                    result.append(text1[i-1])
                    i -= 1
                else:
                    result.append(text2[j-1])
                    j -= 1
        while i > 0:
            result.append(text1[i-1])
            i -= 1
        while j > 0:
            result.append(text2[j-1])
            j -= 1
        return "".join(result[::-1])