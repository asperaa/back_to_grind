"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""547. Friend Circles
"""

class Solution:

    def findCircleNum(self, grid):
        n = len(grid)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                if rank[rx] < rank[ry]:
                    parent[rx] = ry
                elif rank[rx] > rank[ry]:
                    parent[ry] = rx
                else:
                    parent[rx] = ry
                    rank[ry] += 1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and i != j:
                    union(i, j)
        return len({find(x) for x in parent})
