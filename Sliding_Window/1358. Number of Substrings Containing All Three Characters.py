"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1358. Number of Substrings Containing All Three Characters
"""

class Solution:

    def numberOfSubstrings(self, s):
        n = len(s)
        start = 0 # start will always be 0 because there is no upper bound of the number of "a", "b", "c".
        sub_start = 0
        ans = 0
        freq = {"a": 0, "b": 0, "c": 0}
        for end in range(n):
            freq[s[end]] += 1
            while (freq["a"] != 0 and freq["b"] != 0 and freq["c"] != 0):
                freq[s[sub_start]] -= 1
                sub_start += 1
            ans += sub_start - start
        return ans
