"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""764. Largest Plus Sign
"""

class Solution:

    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        dp = [[0 for _ in range(N)]for _ in range(N)]
        ans = 0
        for i in range(N):
            
            count = 0
            for j in range(N):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                dp[i][j] = count
            
            count = 0
            for j in range(N-1, -1, -1):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                dp[i][j] = count if count < dp[i][j] else dp[i][j]
        
        for j in range(N):
        
            count = 0
            for i in range(N):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                dp[i][j] = count if count < dp[i][j] else dp[i][j]
        
            count = 0
            for i in range(N-1, -1, -1):
                if (i, j) in banned:
                    count = 0
                else:
                    count += 1
                dp[i][j] = count if count < dp[i][j] else dp[i][j]
                ans = max(ans, dp[i][j])
        return ans
