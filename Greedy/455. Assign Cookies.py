"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""455. Assign Cookies
"""

class Solution:

    def findContentChildren(self, g, s):
        g = sorted(g)
        s = sorted(s)
        i = j = count = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1
        return count