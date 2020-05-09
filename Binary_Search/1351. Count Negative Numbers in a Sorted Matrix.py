"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1351. Count Negative Numbers in a Sorted Matrix
"""

class Solution:

    def countNegatives(self, grid):
        m, n = len(grid), len(grid[0])
        i, j = 0, n-1
        negatives = 0
        while i <= m-1 and j >= 0:
            if grid[i][j] < 0:
                negatives += m - i
                j -= 1
            else:
                i += 1
        return negatives 