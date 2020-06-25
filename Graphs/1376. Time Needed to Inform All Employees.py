"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1376. Time Needed to Inform All Employees
"""

class Solution:
    
    def numOfMinutes(self, n, headID, manager, informTime):
        G = {i: [] for i in range(n)}
        for i in range(n):
            if manager[i] == -1:
                continue
            G[manager[i]].append(i)
        self.time = 0

        def dfs(i, curr_time):
            self.time = max(self.time, curr_time)
            for neighbour in G[i]:
                dfs(neighbour, curr_time + informTime[neighbour])
        
        dfs(headID, informTime[headID])
        return self.time

        