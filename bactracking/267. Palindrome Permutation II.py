"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""267. Palindrome Permutation II
"""

from collections import Counter

class Solution:

    def generatePalindromes(self, s):
        kv = Counter(s)
        mid = [k for k, v in kv.items() if v%2==1]
        if len(mid) > 1:
            return []
        self.mid = mid
        half = "".join([k * (v//2) for k, v in kv.items()])
        self.total_length = len(half)
        self.ans = []
        visited = [False for _ in range(self.total_length)]
        self.helper(half, "", visited, 0)
        return self.ans
    
    def helper(self, s, curr_s, visited, count):
        if count == self.total_length:
            mid = self.mid[0] if self.mid else ""
            self.ans.append(curr_s + mid + curr_s[::-1])
        else:
            for i in range(self.total_length):
                if not visited[i]:
                    if i > 0 and not visited[i-1] and s[i] == s[i-1]:
                        continue
                    visited[i] = True
                    self.helper(s, curr_s + s[i], visited, count+1)
                    visited[i] = False
    