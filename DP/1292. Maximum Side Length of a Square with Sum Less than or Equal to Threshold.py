"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
"""

class Solution:

    def maxSideLength(self, grid, threshold):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        summ = [[0 for _ in range(n+1)]for _ in range(m+1)]
        length = 1
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                summ[i][j] = grid[i-1][j-1] + summ[i-1][j] + summ[i][j-1] - summ[i-1][j-1]
                if i >= length and j >= length and summ[i][j] - summ[i-length][j] - summ[i][j-length] + summ[i-length][j-length] <= threshold:
                    ans = length
                    length += 1
        return ans