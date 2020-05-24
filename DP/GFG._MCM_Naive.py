"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""MCM [Naive]
"""

def mcm_helper(num, i, j):
    if i >= j:
        return 0
    min_cost = float('inf')
    for k in range(i, j):
        left_cost = mcm_helper(num, i, k)
        right_cost = mcm_helper(num, k+1, j)
        curr_cost = num[i-1] * num[k] * num[j]
        total_cost = left_cost + right_cost + curr_cost
        min_cost = min(min_cost, total_cost)
    return min_cost

def mcm(arr, m):
    return mcm_helper(arr, 1, m-1)

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        m = int(input())
        arr = [int(i) for i in input().split()]
        print(mcm(arr, m))
        t -= 1