"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1079. Letter Tile Possibilities
"""

class Solution:

    def numTilePossibilities(self, s):
        n = len(s)
        s = sorted(s)
        self.total_length = n
        self.ans = 0
        visited = [False for i in range(n)]
        self.helper(s, visited, 0)
        return self.ans
    
    def helper(self, s, visited, count):
        self.ans += 1
        if count == self.total_length:
            return
        else:
            for i in range(self.total_length):
                if not visited[i]:
                    if i > 0 and not visited[i-1] and s[i] == s[i-1]:
                        continue
                    visited[i] = True
                    self.helper(s, visited, count+1)
                    visited[i] = False
        
