"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""947. Most Stones Removed with Same Row or Column [Union Find]
"""

class Solution:

    def removeStones(self, stones):
        self.count = n = len(stones)
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
                self.count -= 1
        
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        return n - self.count
