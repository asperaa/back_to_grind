"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1234. Replace the Substring for Balanced String
"""

from collections import Counter

class Solution:

    def balancedString(self, s):
        n = len(s)
        req_freq = n // 4
        count = Counter(s)
        remove_count = {}
        for key, val in count.items():
            if val > req_freq:
                remove_count[key] = val - req_freq
        min_size = 0
        start = 0
        match_freq = {}
        for end in range(n):
            if s[end] in remove_count:
                match_freq[s[end]] = match_freq.get(s[end], 0) + 1
            while check(remove_count, match_freq):
                min_size = min(min_size, end - start + 1)
                match_freq[s[start]] -= 1
                start += 1
        return min_size
    
    def check(self, remove_count, match_freq):
        for key, val in remove_count.items():
            if remove_count[key] > match_freq[key]:
                return False
        return True

