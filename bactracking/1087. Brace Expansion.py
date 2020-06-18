"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1087. Brace Expansion
"""

class Solution:
    
    def expand(self, s):
        self.ans = []
        self.helper(s, "")
        self.ans.sort()
        return self.ans
    
    def helper(self, s, curr_s):
        if not s:
            self.ans.append(curr_s)
        else:
            if s[0] == "{":
                i = s.find("}")
                for c in s[1:i].split(","):
                    self.helper(s[i+1:], curr_s + c)
            else:
                self.helper(s[1:], curr_s + s[0])