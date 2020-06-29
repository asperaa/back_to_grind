"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""531. Lonely Pixel I
"""

class Solution:

    def findLonelyPixel(self, grid):
        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "B":
                    col[j] += 1
                    row[i] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "B" and col[j] == 1 and row[i] == 1:
                    count += 1
        return count