"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""474. Ones and Zeroes [Bottom Up]
"""

class Solution:

    def findMaxForm(self, strs, m, n):
        zeroes_and_ones = []
        for s in strs:
            zero_count = one_count = 0
            for c in s:
                if c is "0":
                    zero_count += 1
                else:
                    one_count += 1
            zeroes_and_ones.append((zero_count, one_count))
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len(strs)+1)]
        for i in range(1, len(strs)+1):
            for j in range(m+1):
                for k in range(n+1):
                    if j >= zeroes_and_ones[i-1][0] and k >= zeroes_and_ones[i-1][1]:
                        dp[i][j][k] = max(dp[i-1][j-zeroes_and_ones[i-1][0]][k-zeroes_and_ones[i-1][1]],
                                          dp[i-1][j][k])
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        return dp[len(strs)][m][n]
