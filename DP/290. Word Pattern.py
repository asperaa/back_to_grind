"""We are the captain of our ships, and we stay 'till the end. We see our stories through.
"""

"""290. Word Pattern
"""

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word_map, pattern_map = {}, {}
        words = str.split(" ")
        n = len(words)
        m = len(pattern)
        if m != n:
            return False
        for i in range(n):
            if pattern_map.get(pattern[i], -1) != word_map.get(words[i], -1):
                return False
            pattern_map[pattern[i]] = word_map[words[i]] = i
        return True
        