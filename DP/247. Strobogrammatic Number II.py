"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""247. Strobogrammatic Number II
"""

class Solution:

    def findStrobogrammatic(self, n):
        self.hash = {"0":"0", 1:1, 6:9, 8:8, 9:6}
        self.ans = []
        num = [None] * n
        self.helper(0, n-1, num)
        return self.ans
    
    def helper(self, start, end, num):
        if start > end:
            self.ans.append("".join(num))
            return
        for key in self.hash:
            if start == end and key in ("6", "9"):
                continue
            if start != end and start == 0 and key == "0":
                continue 
            num[start] = key
            num[end] = self.hash[key]
            self.helper(start+1, end-1, num)