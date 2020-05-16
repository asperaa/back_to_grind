"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""01 Knapsack [Bottom up]
"""




def knapsack(weights, values, C):
    length = len(weights)
    dp = ([[0] * (C + 1)]) * (length + 1)
    for i in range(1, length+1):
        for j in range(1, C+1):
            if weights[i-1] <= j:
                dp[i][j] = max(values[i-1] + dp[i-1][j-weights[i-1]], dp[i-1][j])   
            elif weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
    return dp[length][C]

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        capacity = int(input())
        values = [int(i) for i in input().split()]
        weight = [int(i) for i in input().split()]
        print(knapsack(weight, values, capacity))
        t -= 1