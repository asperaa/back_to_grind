"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""323. Number of Connected Components in an Undirected Graph [Union Find]
"""

class Solution:

    def countComponents(self, n, edges):
        parent = list(range(n))
        rank = [0] * n

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                if rank[rx] > rank[ry]:
                    parent[ry] = rx
                elif rank[rx] < rank[ry]:
                    parent[rx] = ry
                else:
                    parent[rx] = ry
                    rank[ry] += 1
        for u, v in edges:
            union(u, v)
        return len({find(x) for x in range(n)}) 