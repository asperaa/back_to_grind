"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""22. Generate Parentheses
"""

class Solution:

    def generateParenthesis(self, n):
        self.ans = []
        self.helper(n, n, "")
        return self.ans

    def helper(self, left_remain, right_remain, arrangement):
        if left_remain > right_remain or left_remain < 0 or right_remain < 0:
            return
        if left_remain == 0 and right_remain == 0:
            self.ans.append(arrangement)
        self.helper(left_remain - 1, right_remain, arrangement + "(")
        self.helper(left_remain, right_remain - 1, arrangement + ")")