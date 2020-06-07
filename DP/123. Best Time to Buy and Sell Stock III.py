"""123. Best Time to Buy and Sell Stock III
"""

class Solution:

    def maxProfit(self, prices):
        if not prices:
            return 0
        s1 = s2 = s3 = s4 = float('-inf')
        for i in range(len(prices)):
            s1 = max(s1, 0 - prices[i])
            s2 = max(s2, s1 + prices[i])
            s3 = max(s3, s2 - prices[i])
            s4 = max(s4, s3 + prices[i])
        return max(0, s4)