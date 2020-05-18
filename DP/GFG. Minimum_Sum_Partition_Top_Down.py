"""We are the captains of our ships, and we stauy 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/minimum-sum-partition/0
[Top Down]
"""

def min_sum_partition_helper(nums, dp, n, curr_sum, total_sum):
    if dp[n][curr_sum]:
        return dp[n][curr_sum]
    if n == 0:
        return abs(total_sum - 2 * curr_sum)
    dp[n][curr_sum] = min(
        min_sum_partition_helper(nums, dp, n-1, curr_sum + nums[n-1], total_sum),
        min_sum_partition_helper(nums, dp, n-1, curr_sum, total_sum)
    )
    return dp[n][curr_sum]

def min_sum_part(nums, n):
    total_sum = sum(nums)
    dp = [[None for _ in range(total_sum + 1)] for _ in range(n + 1)]
    return min_sum_partition_helper(nums, dp, n, 0, total_sum)

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        nums = [int(i) for i in input().split()]
        print(min_sum_part(nums, n))
        t -= 1
