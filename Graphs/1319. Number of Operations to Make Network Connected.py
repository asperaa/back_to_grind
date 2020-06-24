"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1319. Number of Operations to Make Network Connected
"""

class Solution:

    def makeConnected(self, n, edges):
        n = len(edges)
        parent = list(range(n))
        rank = [0] * n
        count_redundant = 0

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
            else:
                count_redundant += 1
        
        for u, v in edges:
            union(u, v)
        connected_components = len({find(x) for x in range(n)})
        if connected_components - 1 <= count_redundant:
            return connected_components - 1
        return -1 
