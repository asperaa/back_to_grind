"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""684. Redundant Connection
"""

class Solution:

    def findRedundantConnection(self, edges):
        nodes = len(edges)
        parent = list(range(nodes + 1))
        rank = [0] * (nodes + 1)

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return True
            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[rx] = ry
                rank[ry] += 1
            return False

        for u, v in edges:
            if union(u, v):
                return (u, v)
        
                