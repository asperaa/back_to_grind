"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1312. Minimum Insertion Steps to Make a String Palindrome
"""

class Solution:

    def minInsertions(self, s):
        rev_s = s[::-1]
        m = len(s)
        dp = [[0 for _ in range(m+1)]for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, m+1):
                if s[i-1] == rev_s[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return m - dp[m][m]
