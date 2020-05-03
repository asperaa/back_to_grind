"""We are the captains of our ships and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0
   [Naive Recursion]
"""


def knapsack(weight, value, capacity):
    number_of_items = len(weight)
    return knapsack_helper(number_of_items-1, 0, weight, value, capacity)


def knapsack_helper(n, curr_weight, weight, value, capacity):
    if n == -1 or capacity == 0:
        return 0
    if curr_weight + weight[n] > capacity:
        return knapsack_helper(n-1, curr_weight, weight, value, capacity)
    left = value[n] + knapsack_helper(n-1, curr_weight+weight[n], weight, value, capacity)
    right = knapsack_helper(n-1, curr_weight, weight, value, capacity)
    return max(left, right)

if __name__ == "__main__":
    w = [100, 20, 200, 5]
    v = [100, 10, 0, 200]
    c = 0
    print(knapsack(w, v, c))
