"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""368. Largest Divisible Subset
"""

class Solution:
    
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        n = len(nums)
        nums = sorted(nums)
        dp = [(1, -1) for _ in range(n)]
        largest_length, largest_index = float('-inf'), -1
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i] = (dp[j][0] + 1, j)
            if dp[i][0] > largest_length:
                largest_length = dp[i][0]
                largest_index = i
        result = []
        k = largest_index
        while True:
            result.append(nums[k])
            k = dp[k][1]
            if k == -1:
                break
        return result[::-1]