"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""248. Strobogrammatic Number III
"""

class Solution:

    def strobogrammaticInRange(self, low, high):
        self.ans = []
        self.hash = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        for i in range(len(low), len(high)+1):
            num = [None] * i
            self.helper(0, i-1, num)
        return self.ans
    
    def helper(self, start, end, num):
        if start > end:
            self.ans.append("".join(num))
            return
        for key in self.hash:
            if start == end and key in (6, 9):
                continue
            if start != end and start == 0 and key == "0":
                continue
            num[start] = key
            num[end] = self.hash[key]
            self.helper(start+1, end-1, num)