
def knapsack(weight, value, capacity):
    num_items = len(weight)
    dp = [[-1]*(capacity + 1)]*(num_items)
    return knapsack_helper(num_items-1, 0, weight, value, capacity, dp)

def knapsack_helper(n, curr_weight, weight, value, capacity, dp):
    if n == -1 or capacity == 0:
        return 0
    if curr_weight + weight[n] > capacity:
        dp[n][curr_weight] = knapsack_helper(n-1, curr_weight, weight, value, capacity, dp)
    if curr_weight + weight[n] < capacity:
        chosen = value[n] + knapsack_helper(n-1, curr_weight + weight[n], weight, value, capacity, dp)
        not_chosen = knapsack_helper(n-1, curr_weight,weight, value, capacity, dp)
        dp[n][curr_weight] = max(chosen, not_chosen)
        return dp[n][curr_weight]
    