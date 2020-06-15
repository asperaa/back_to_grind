"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1291. Sequential Digits
"""

class Solution:

    def sequentialDigits(self, low, high):
        self.ans = []
        self.low = low
        self.high = high
        for i in range(1, 9):
            self.helper(i, i)
        return sorted(self.ans)
    
    def helper(self, num, last_digit):
        if num >= self.low and num <= self.high:
            self.ans.append(num)
        if last_digit == 9:
            return