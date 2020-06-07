"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""188. Best Time to Buy and Sell Stock IV
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if k >= n // 2:
            return self.quick_solve(prices)
        states = [0] + [float('-inf') for _ in range(2*k)]
        for i in range(n):
            for j in range(k):
                states[2*j + 1] = max(states[2*j + 1], states[2*j] - prices[i])
                states[2*j + 2] = max(states[2*j + 2], states[2*j+1] + prices[i])
        return max(0, states[-1])
    def quick_solve(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
                