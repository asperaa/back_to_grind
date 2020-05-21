"""We are thecaptains of our ships, and we stay 'till the end. We see our stories through.
"""

"""[983. Minimum Cost For Tickets]
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]):
        travel = {}
        for day in days:
            travel[day] = True
        dp = [None for _ in range(366)]
        dp[0] = 0
        for i in range(1, 366):
            if i in travel:
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[365]        
