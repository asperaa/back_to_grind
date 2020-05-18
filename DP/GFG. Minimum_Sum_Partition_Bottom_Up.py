"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/minimum-sum-partition/0
[Bottom Up]
"""

def min_sum_partition(nums, n):
    total_sum = sum(nums)
    dp = [[False for _ in range(total_sum + 1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for j in range(total_sum+1):
        dp[0][j] = False
    for i in range(1, n+1):
        for j in range(1, total_sum+1):
            if j >= nums[i-1]:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    min_diff = float('inf')
    half = total_sum // 2
    for j in range(half, -1, -1):
        if dp[n][j]:
            min_diff = total_sum - 2*j
            break
    return min_diff

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        nums = [int(i) for i in input().split()]
        print(min_sum_partition(nums, n))
        t -= 1