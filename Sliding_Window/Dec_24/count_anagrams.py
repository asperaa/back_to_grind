
from collections import Counter

class Solution:
    def search(self, pat, txt):
        # Initializing pointers and variables
        i = 0
        j = 0
        n = len(txt)
        k = len(pat)
        ans = 0
        
        # Create a hashmap with the frequency of characters in the pattern
        hash_map = Counter(pat)
        count = len(hash_map)
        
        # Sliding window
        while i < n:
            if txt[i] in hash_map:
                hash_map[txt[i]] -= 1
                if hash_map[txt[i]] == 0:
                    count -= 1
            
            if i - j + 1 < k:
                i += 1
            elif i - j + 1 == k:
                if count == 0:
                    ans += 1
                if txt[j] in hash_map:
                    if hash_map[txt[j]] == 0:
                        count += 1
                    hash_map[txt[j]] += 1
                j += 1
                i += 1
        
        return ans