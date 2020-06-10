"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""784. Letter Case Permutation
"""

class Solution:
    
    def letterCasePermutation(self, s):
        s = s.lower()
        n = len(s)
        self.total_length = n
        self.ans = []
        self.helper(s, s, 0)
        return self.ans
    
    def helper(self, s, curr_s, curr_index):
        if curr_index == self.total_length:
            self.ans.append(curr_s)
            return
        if s[curr_index].isnumeric():
            self.helper(s, curr_s, curr_index+1)
            return
        self.helper(s, curr_s[:curr_index]+curr_s[curr_index].upper()+curr_s[curr_index+1:], curr_index+1)
        self.helper(s, curr_s, curr_index+1)


