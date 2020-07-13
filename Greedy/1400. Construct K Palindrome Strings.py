"""We are the capatains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1400. Construct K Palindrome Strings
"""

from collections import Counter

class Solution:

    def canConstruct(self, s, k):
        count = Counter(s)
        odds = even = 0
        for freq in count.values():
            if freq % 2 == 1:
                odds += 1
        return k <= len(s) and odds <= k
