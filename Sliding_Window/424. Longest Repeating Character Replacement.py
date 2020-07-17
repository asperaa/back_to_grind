"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""424. Longest Repeating Character Replacement
"""

class Solution:

    def characterReplacement(self, s, k):
        start = 0
        count = [0 for _ in range(26)]
        n = len(s)
        max_size = local_max_freq = 0
        for end in range(n):
            count[ord(s[end])- ord('A')] += 1
            local_max_freq = max(local_max_freq, count[ord(s[end]) - ord('A')])
            replace_freq = end - start + 1 - local_max_freq
            if replace_freq > k:
                count[ord(s[start]) - ord('A')] -= 1
                start += 1
            else:
                max_size = max(max_size, end - start + 1)
        return max_size
