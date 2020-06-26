"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1101. The Earliest Moment When Everyone Become Friends
"""

class Solution:

    def earliestAcq(self, logs, n):
        logs = sorted(logs)
        parent = [list(range(n))]
        rank = [0] * n
        self.connected_comp = n

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
                self.connected_comp -= 1
        
        for time, u, v in logs:
            union(u, v)
            if self.connected_comp == 1:
                return time
        return -1

