"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""247. Strobogrammatic Number II
"""

class Solution:
    
    def strobogrammaticInRange(self, low, high):
        self.ans = 0
        self.hash = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        self.low = int(low)
        self.high = int(high)
        for i in range(len(low), len(high)+1):
            num = [None] * i
            self.helper(0, i-1, num)
        return self.ans
    
    def helper(self, start, end, num):
        if start > end:
            sto_num = int("".join(num))
            if sto_num >= self.low and sto_num <= self.high:
                self.ans += 1
            return
        for key in self.hash:
            if start == end and key in ("6", "9"):
                continue
            if start != end and start == 0 and key == "0":
                continue
            num[start] = key
            num[end] = self.hash[key]
            self.helper(start+1, end-1, num)