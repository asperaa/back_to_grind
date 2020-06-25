"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""261. Graph Valid Tree
"""

class Solution:
    

    def validTree(self, n, edges):
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
                elif rank[ry] < rank[rx]:
                    parent[ry] = rx
                else:
                    parent[rx] = ry
                    rank[ry] += 1
                return True
            else:
                return False
        
        for u, v in edges:
            if not union(u, v):
                return False
        return len({find(x) for x in parent}) == 1