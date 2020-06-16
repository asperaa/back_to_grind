"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
"""

def findPath(arr, n):
    ans = []
    visited = [[False for _ in range(n)]for _ in range(n)]
    make_path(arr, 0, 0, "", n, visited, ans)
    return ans

def make_path(arr, i, j, path, n, visited, ans):
    if not valid(arr, i, j, n, visited):
        return
    visited[i][j] = True
    if i == n-1 and j == n-1:
        ans.append(path)
    make_path(arr, i, j+1, path + "R", n, visited, ans)
    make_path(arr, i+1, j, path + "D", n, visited, ans)
    make_path(arr, i, j-1, path + "L", n, visited, ans)
    make_path(arr, i-1, j, path + "U", n, visited, ans)
    visited[i][j] = False

def valid(arr, i, j, n, visited):
    if i >= 0 and j >= 0 and i < n and j < n and not visited[i][j] and arr[i][j] == 1:
        return True
    return False