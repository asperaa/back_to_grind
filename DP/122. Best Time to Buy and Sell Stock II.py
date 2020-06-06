"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""122. Best Time to Buy and Sell Stock II
"""

class Solution:

    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit