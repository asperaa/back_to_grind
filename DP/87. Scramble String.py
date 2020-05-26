"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""87. Scramble String
"""

class Solution:
    
    def isScramble(self, s1, s2):
        if s1 == "":
            return True
        cache = {}
        return self.isScrambleHelper(s1, s2, cache)

    def isScrambleHelper(self, s1, s2, cache):
        if s1 == s2:
            return True
        length = len(s1)
        if length <= 1:
            return False
        key = s1 + '_' + s2
        if key in cache:
            return cache[key]
        is_scramble = False
        for k in range(1, length):
            if (self.isScrambleHelper(s1[:k], s2[-k:], cache) and self.isScrambleHelper(s1[k:], s2[:length-k], cache)) or \
               (self.isScrambleHelper(s1[:k], s2[:k], cache) and self.isScrambleHelper(s1[k:], s2[k:], cache)):
               is_scramble = True
               break
        cache[key] = is_scramble
        return is_scramble
