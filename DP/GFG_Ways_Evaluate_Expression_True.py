"""We are the captains of our ships, and we stay 'till the end. We see our stories through. 
"""

"""GFG_Ways_To_Evaluate_Expression_To_True
"""

def boolean_parent(s, m):
    dp = [[[None for _ in range(m+1)]for _ in range(m+1)]for _ in range(2)]
    return boolean_parent_helper(s, 0, m-1, True, dp)

def boolean_parent_helper(s, i, j, is_True, dp):
    if i > j:
        return 0
    if i == j:
        if is_True:
            return 1 if s[i] == 'T' else 0
        else:
            return 1 if s[i] == 'F' else 0
    if is_True and dp[1][i][j]:
        return dp[1][i][j]
    if is_True == False and dp[0][i][j]:
        return dp[0][i][j]
    num_ways = 0
    for k in range(i+1, j, 2):
        lt = boolean_parent_helper(s, i, k-1, True, dp)
        lf = boolean_parent_helper(s, i, k-1, False, dp)
        rt = boolean_parent_helper(s, k+1, j, True, dp)
        rf = boolean_parent_helper(s, k+1, j, False, dp)
        if s[k] == '|':
            if is_True:
                num_ways += lt * rt + lt * rf + rt * lf
            else:
                num_ways += lf * rf
        elif s[k] == '&':
            if is_True:
                num_ways += lt * rt
            else:
                num_ways += lf * rt + rf * lt + rf * lf
        elif s[k] == '^':
            if is_True:
                num_ways += lf * rt + rf * lt
            else:
                num_ways += lt * rt + lf * rf
    if is_True:
        dp[1][i][j] = num_ways
    else:
        dp[0][i][j] = num_ways
    return num_ways

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        m = int(input())
        s = input()
        print(boolean_parent(s, m))
        t -= 1


    