"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""990. Satisfiability of Equality Equations
"""

class Solution:
    
    def equationsPossible(self, edges):

        parent = list(range(26))
        rank = [0] * 26

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
        
        not_equals = []
        for edge in edges:
            if edge[1:3] == "==":
                union(ord(edge[0]) - ord('a'), ord(edge[3]) - ord('a'))
            else:
                not_equals.append(edge)
        
        for edge in not_equals:
            rx, ry = find(ord(edge[0]) - ord('a')), find(ord(edge[3]) - ord('a'))
            if rx == ry:
                return False
        return True



