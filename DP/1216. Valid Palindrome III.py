"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1216. Valid Palindrome III
"""
class Solution:

    def isValidPalindrome(self, s, k):
        length = len(s)
        rev_s = s[::-1]
        dp = [[0 for _ in range(length + 1)]for _ in range(length+1)]
        for i in range(1, length+1):
            for j in range(1, length+1):
                if s[i-1] == rev_s[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        number_of_deletions = length - dp[length][length]
        return number_of_deletions <= k
