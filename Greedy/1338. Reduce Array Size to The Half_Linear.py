"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1338. Reduce Array Size to The Half [Linear]
"""
from collections import Counter

class Solution:

    def minSetSize(self, arr):
        n = len(arr)
        count = Counter(arr)
        freq = [[] for _ in range(n+1)]
        for key, val in count.items():
            freq[val].append(key)
        ans = cuts = 0
        for i in range(n, -1, -1):
            if not freq[i]:
                continue
            for _ in freq[i]:
                cuts += i
                ans += 1
                if cuts >= n // 2:
                    return ans
