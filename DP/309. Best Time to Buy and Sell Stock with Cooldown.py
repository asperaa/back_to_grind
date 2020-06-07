"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""309. Best Time to Buy and Sell Stock with Cooldown
"""

class Solution:

    def maxProfit(self, prices):
        n = len(prices)
        held = [float('-inf') for _ in range(n+1)]
        sold = [float('-inf') for _ in range(n+1)]
        reset = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            reset[i] = max(reset[i-1], sold[i-1])
            held[i] = max(held[i-1], reset[i-1] - prices[i-1])
            sold[i] = held[i-1] + prices[i-1]
        return max(sold[n], reset[n])