"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""376. Wiggle Subsequence [Walked through fire]
"""

class Solution:
    
    def wiggleMaxLength(self, nums):
        n = len(nums)
        if n < 2:
            return n
        dp = [(2, True) for i in range(n)]
        for i in range(1, n):
            if nums[i] < nums[0]:
                dp[i] = (2, False)
            if nums[i] == nums[0]:
                dp[i] = (1, False)
        maxx_length = 1
        for i in range(2, n):
            for j in range(1, i):
                if dp[j][1] == False:
                    if nums[i] > nums[j] and dp[i][0] < dp[j][0] + 1:
                        dp[i] = (dp[j][0] + 1, True)
                elif dp[j][1] == True:
                    if nums[i] < nums[j] and dp[i][0] < dp[j][0] + 1:
                        dp[i] = (dp[j][0] + 1, False)
                maxx_length = max(maxx_length, dp[i][0])
        return maxx_length
                        
