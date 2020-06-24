"""We are the captains of our ships, an we stay 'till the end. We see our stories through. 
"""

"""947. Most Stones Removed with Same Row or Column
"""

class Solution:
    
    def removeStones(self, stones):
        visited = {tuple(stone): False for stone in stones}
        
        def dfs(s1, visited):

            visited[s1] = True
            for s2 in stones:
                s2 = tuple(s2)
                if not visited[s2]:
                    if (s2[0] == s1[0] or s2[1] == s1[1]):
                        visited[s2] = True
                        dfs((s2[0], s2[1]), visited)
        
        connected_components = 0
        for stone in stones:
            s = tuple(stone)
            if not visited[s]:
                dfs(s, visited)
                connected_components += 1
        return len(stones) - connected_components


