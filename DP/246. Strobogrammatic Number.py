"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""246. Strobogrammatic Number
"""

class Solution:
    
    def isStrobogrammatic(self, num):
        hash = set([("1", "1"), ("0", "0"), ("8", "8"), ("6", "9"), ("9", "6")])
        start, end = 0, len(num)-1
        while start <= end:
            if (num[start], num[end]) not in hash:
                return False
            start += 1
            end -= 1
        return True