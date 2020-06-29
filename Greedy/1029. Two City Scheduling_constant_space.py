"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1029. Two City Scheduling
"""

class Solution:

    def twoCitySchedCost(self, costs):
        costs.sort(key = lambda x:(x[1]-x[0]), reverse=True)
        n = len(costs) // 2
        min_cost = 0
        for i in range(n):
            min_cost += costs[i][0]
        for i in range(n, 2*n):
            min_cost += costs[i][1]
        return min_cost
