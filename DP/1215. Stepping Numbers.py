"""We are the captains of our ships, and we sty 'till the end. We see our stories through.
"""

"""1215. Stepping Numbers
"""

class Solution:
    def countSteppingNumbers(self, low: int, high: int):
        self.ans = []
        for i in range(10):
            if i == 1: # 1 comes 2 times (i.e dfs from 0 gives 1 too)
                continue
            self.helper(low, high, i)
        return sorted(self.ans)
    
    def helper(self, low, high, num):
        if num > high:
            return
        if num >= low:
            self.ans.append(num)
        last_digit = num % 10
        if last_digit == 0:
            self.helper(low, high, num*10 + last_digit + 1)
        elif last_digit == 9:
            self.helper(low, high, num*10 + last_digit - 1)
        else:
            self.helper(low, high, num*10 + last_digit + 1)
            self.helper(low, high, num*10 + last_digit - 1)
        

        