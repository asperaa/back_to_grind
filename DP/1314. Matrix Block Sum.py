"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1314. Matrix Block Sum
"""

class Solution:

    def matrixBlockSum(self, grid, k):
        m, n = len(grid), len(grid[0])
        summ = [[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                summ[i][j] = grid[i-1][j-1] + summ[i-1][j] + summ[i][j-1] - summ[i-1][j-1]
        for i in range(m):
            for j in range(n):
                r1 = max(0, i-k)
                c1 = max(0, j-k)
                r2 = min(m-1, i+k)
                c2 = min(n-1, j+k)
                r1 +=1
                c1 += 1
                r2 += 1
                c2 += 1
                grid[i][j] = summ[r2][c2] - summ[r2][c1-1] - summ[r1-1][c2] + summ[r1-1][c1-1]
        return grid 