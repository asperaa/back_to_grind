"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1049. Last Stone Weight II [Bottom Up]
"""

class Solution:
    
    def lastStoneWeightII(self, stones):
        total_sum = sum(stones)
        length = len(stones)
        dp = [[None for _ in range(total_sum+1)] for _ in range(length + 1)]
        for i in range(length+1):
            dp[i][0] = True
        for j in range(1, total_sum+1):
            dp[0][j] = False
        for i in range(1, length+1):
            for j in range(1, total_sum+1):
                if j >= stones[i-1]:
                    dp[i][j] = dp[i-1][j-stones[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        S = float('-inf')
        for j in range(total_sum//2):
            if dp[length][j]:
                S = max(S, j)
        return total_sum - 2 * S