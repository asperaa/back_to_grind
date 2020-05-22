"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1143. Longest Common Subsequence [Naive]
"""


class Solution:

    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        return self.lcs_helper(text1, text2, m, n)

    def lcs_helper(self, text1, text2, m, n):
        if m == 0 or n == 0:
            return 0
        if text1[m-1] == text2[n-1]:
            return 1 + self.lcs_helper(text1, text2, m-1, n-1)
        else:
            return max(self.lcs_helper(text1, text2, m, n-1), self.lcs_helper(text1, text2, m-1, n))
        