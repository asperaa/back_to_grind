"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0
   [Memoization]
"""

def knapsack(weight, value, capacity):
    number_of_items = len(weight)
    dp = [[-1] * (capacity + 1)] * number_of_items 
    return knapsack_helper(weight, value, capacity, number_of_items - 1)


def knapsack_helper(dp, weight, value, C, n):
    if C == 0 or n == -1:
        return 0
    if dp[n][C] != -1:
        return dp[n][C]
    take_curr_weight = 0
    if C - weight[n] >= 0:
        take_curr_weight = value[n] + knapsack_helper(weight, value, C - weight[n], n-1)
    leave_curr_weight = knapsack_helper(weight, value, C, n-1)
    dp[n][C] = max(take_curr_weight, leave_curr_weight)
    return max(take_curr_weight, leave_curr_weight)

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        capacity = int(input())
        values = [int(i) for i in input().split()]
        weight = [int(i) for i in input().split()]
        print(knapsack(weight, values, capacity))
        t -= 1
