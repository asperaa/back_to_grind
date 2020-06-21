"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""841. Keys and Rooms
"""

class Solution:
    
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [0 for _ in range(n)]
        
        def dfs(i):
            if visited[i] == 1:
                return
            visited[i] = 1
            for neighbour in rooms[i]:
                dfs(neighbour)

        dfs(0)
        return sum(visited) == n
        