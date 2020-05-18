"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1221. Split a String in Balanced Strings
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R = L = 0
        count = 0
        for c in s:
            if c == 'R':
                R += 1
            elif c == 'L':
                L += 1
            if R == L:
                R = 0
                L = 0
                count += 1
        return count
        
        