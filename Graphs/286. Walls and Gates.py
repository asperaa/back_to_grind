"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1091. Shortest Path in Binary Matrix
"""

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        queue = deque()
        queue.append((0, 0, 1))
        while queue:
            x, y, d = queue.popleft()
            if x == m-1 and y == n-1:
                return d
            for dirr in directions:
                new_x, new_y = x + dirr[0], y + dirr[1]
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 0:
                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y, d+1))
        return -1
        
        