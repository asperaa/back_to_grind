"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""132. Palindrome Partitioning II
"""

class Solution:
    
    def minCut(self, s):
        m = len(s)
        palin = [[False for _ in range(m+1)]for _ in range(m+1)]
        dp = [[None for _ in range(m+1)]for _ in range(m+1)]
        return self.min_cut_helper(s, 0, m-1, dp, palin)

    def is_palindrome(self, s, i, j, palin):
        if s[i] == s[j] and (j == i+1 or palin[i+1][j-1]):
            palin[i][j] = True
            return True
        while i < j:
            if s[i] != s[j]:
                palin[i][j] = False
                return False
            i += 1
            j -= 1
        palin[i][j] = True
        return True

    def min_cut_helper(self, s, i, j, dp, palin):
        if i >= j:
            return 0
        if dp[i][j]:
            return dp[i][j]
        if self.is_palindrome(s, i, j, palin):
            return 0
        min_cuts = float('inf')
        for k in range(i, j):
            if dp[i][k]:
                left_cut = dp[i][k]
            else:
                left_cut = self.min_cut_helper(s, i, k, dp, palin)
                dp[i][k] = left_cut
            if dp[k+1][j]:
                right_cut = dp[k+1][j]
            else:
                right_cut = self.min_cut_helper(s, k+1, j, dp, palin)
                dp[k+1][j] = right_cut
            total_temp_parts = left_cut + right_cut + 1
            min_cuts = min(min_cuts, total_temp_parts)
        dp[i][j] = min_cuts
        return min_cuts


if __name__ == "__main__":
    s = Solution()
    print(s.is_palindrome("AAB", 0, 2))

        
