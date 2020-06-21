"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""463. Island Perimeter
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += 4
                    if i > 0 and grid[i-1][j]:
                        result -= 2
                    if j > 0 and grid[i][j-1]:
                        result -= 2
        return result