"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""740. Delete and Earn
"""

class Solution:

    def deleteAndEarn(self, nums):
        buckets = [0 for _ in range(10001)]
        for num in nums:
            buckets[num] += num
        dp = [0 for _ in range(10001)]
        dp[0] = buckets[0]
        dp[1] = buckets[1]
        for i in range(2, 10001):
            dp[i] = max(buckets[i] + dp[i-2], dp[i-1])
        return dp[10000]
