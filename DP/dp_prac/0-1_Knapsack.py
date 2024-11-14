"We are the captains of our ships, we stay 'till the end. We see our stories through."

def knapsack(weight, value, capacity):
    num_items = len(weight)
    return knapsack_helper(num_items-1, 0, weight, value, capacity)

def knapsack_helper(n, curr_weight, weight, value, capacity):
    if n==-1 or capacity == 0:
        return 0
    if curr_weight + weight[n] > capacity:
        return knapsack_helper(n-1, curr_weight, weight, value, capacity)
    
    if curr_weight + weight[n] < capacity:
        chosen = value[n] + knapsack_helper(n-1, curr_weight + weight[n], weight, value, capacity)
        not_chosen = knapsack_helper(n, curr_weight, weight, value, capacity)
        return max(chosen, not_chosen)
if __name__ == "__main__":
    value = []
    weight = []
    capacity = 40
    knapsack(weight, value, capacity)