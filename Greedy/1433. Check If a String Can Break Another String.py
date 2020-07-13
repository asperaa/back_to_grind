"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1433. Check If a String Can Break Another String [T - O(nlogn)]
"""

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ls1 = sorted([c for c in s1])
        ls2 = sorted([c for c in s2])
        n = len(s1)
        can_break = True
        for i in range(n):
            if ord(ls1[i]) < ord(ls2[i]):
                can_break = False
                break
        if can_break:
            return True
        can_break = True
        for i in range(n):
            if ord(ls2[i]) < ord(ls1[i]):
                can_break = False
                break
        if can_break:
            return True
        return False
        
