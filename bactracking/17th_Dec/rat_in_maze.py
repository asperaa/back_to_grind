"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
"""

def findPath(arr, n):
    ans = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    helper(arr, n, visited, 0, 0, "", ans)
    return ans

def valid(i, j, visited, arr, n):
    if i >=0 and j >= 0 and i < n and j < n and not visited[i][j] and arr[i][j] == 1:
        return True 

def helper(arr, n, visited, i, j, path, ans):
    if not valid(i, j, visited, arr, n):
        return
    visited[i][j] = True
    if i == n-1 and j == n-1:
        ans.append(path)
    
    helper(arr, n, visited, i, j+1, path + "R", ans)
    helper(arr, n, visited, i, j-1, path + "L", ans)
    helper(arr, n, visited, i-1, j, path + "U", ans)
    helper(arr, n, visited, i+1, j, path + "D", ans)
    
    visited[i][j] = False

    
