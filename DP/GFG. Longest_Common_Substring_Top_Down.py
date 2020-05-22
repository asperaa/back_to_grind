"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""Longest Common Substring [Top Down]
"""

def lcs(X, Y, i, j, count) :  
      
    if (i == 0 or j == 0) :  
        return count  
    if (X[i - 1] == Y[j - 1]) : 
        count = lcs(i - 1, j - 1, count + 1)  
    count = max(count, max(lcs( i, j - 1, 0),  
                           lcs( i - 1, j, 0)))  
    return count 