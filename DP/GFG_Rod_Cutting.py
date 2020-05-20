"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
[Naive Recursion]
"""

def rod_cut_helper(prices, n, curr_length):
    if n == 0 or curr_length == 0:
        return 0
    if curr_length >= n:
        return max(prices[n-1] + rod_cut_helper(prices, n, curr_length-n),
                   rod_cut_helper(prices, n-1, curr_length))
    elif curr_length < n:
        return rod_cut_helper(prices, n-1, curr_length)

def rod_cut(prices, n):
    return rod_cut_helper(prices, n, n)


if __name__ == "__main__":
    prices = [1, 9, 8] 
    print(rod_cut(prices, len(prices)))