"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1029. Two City Scheduling
"""

class Solution:

    def twoCitySchedCost(self, costs):
        refund = []
        min_cost = 0
        for a, b in costs:
            min_cost += a
            refund.append(b-a)

        n = len(costs)//2
        refund.sort()
        for i in range(n):
            min_cost += refund[i]
        return min_cost