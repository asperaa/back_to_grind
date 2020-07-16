"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""76. Minimum Window Substring
"""

class Solution:
    
    def minWindow(self, s, t):
        t_freq = {}
        r_freq = {}
        min_size = float('inf')
        ans_start = ans_end = -1
        start = 0
        n = len(s)
        for c in t:
            t_freq[c] = 0
            r_freq[c] = r_freq.get(c, 0) + 1
        for end in range(n):
            if s[end] not in t_freq:
                continue
            t_freq[s[end]] += 1
            while self.is_contains(t_freq, r_freq):
                if min_size > end - start + 1:
                    min_size = end - start + 1
                    ans_start = start
                    ans_end = end
                if s[start] in t_freq:
                    t_freq[s[start]] -= 1
                start += 1
        if ans_start == -1:
            return ""
        return s[ans_start: ans_end + 1] 
    
    def is_contains(self, t_freq, r_freq):
        for key, val in t_freq.items():
            if t_freq[key] < r_freq[key]:
                return False
        return True