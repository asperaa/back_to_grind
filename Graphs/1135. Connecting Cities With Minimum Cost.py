"""We are the captains of oue ships, and we stay 'till the end. We see our stories through.
"""

"""1135. Connecting Cities With Minimum Cost
"""

class Solution:

    def minimumCost(self, n ,edges):
        parent = [i for i in range(n+1)]
        rank = [0] * (n+1)
        self.cost = 0
        self.connected_components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y, w):
            rx, ry = find(x), find(y)
            if rx != ry:
                if rank[rx] < rank[ry]:
                    parent[rx] = ry
                elif rank[ry] < rank[rx]:
                    parent[ry] = rx
                else:
                    parent[rx] = ry
                    rank[ry] += 1
                self.connected_components -= 1
                self.cost += w
        
        edges.sort(key=lambda x: x[2])
        for u, v, w in edges:
            union(u, v, w)
            if self.connected_components == 1:
                return self.cost
        return -1