"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""291. Word Pattern II
"""

class Solution:

    def wordPatternMatch(self, pattern, str):
        return self.helper(pattern, str, 0, 0, {}, {})
    
    def helper(self, pattern, str, i, j, p_hash, s_hash):
        if i == len(pattern) and j == len(str):
            return True
        elif i == len(pattern) or j == len(str):
            return False
        else:
            p = pattern[i]
            added = False
            for k in range(j, len(str)):
                word = str[j:k+1]
                if (p in p_hash and p_hash[p] != word) or (word in s_hash and s_hash[word] != p):
                    continue
                if p not in p_hash and word not in s_hash:
                    p_hash[p] = word
                    s_hash[word] = p
                    added = True
                remaining = self.helper(pattern, str, i+1, k+1, p_hash, s_hash)
                if added:
                    del p_hash[p]
                    del s_hash[word]
                if remaining:
                    return True
        return False
