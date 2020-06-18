"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""842. Split Array into Fibonacci Sequence
"""

class Solution:
    
    def splitIntoFibonacci(self, num):
        length = len(num)
        self.ans = []
        for i in range(1, length):
            for j in range(i+1, length):
                self.ans = []
                a = self.parse(num[:i])
                b = self.parse(num[i:j])
                if a == -1 or b == -1:
                    continue
                if self.helper(num[j:], a, b):
                    self.ans.append(b)
                    self.ans.append(a)
                    return self.ans[::-1]
        return []
    
    def helper(self, s, a, b):
        if not s:
            return True
        for i in range(1, len(s)+1):
            c = self.parse(s[:i])
            if c == -1:
                continue
            if c - a == b and self.helper(s[i:], b, c):
                self.ans.append(c)
                return True
        return False
    
    def parse(self, s):
        if s and s[0] == "0" and len(s) != 1:
            return -1
        if not s:
            return -1
        num = int(s)
        if num > (1 << 31) - 1:
            return -1
        return num