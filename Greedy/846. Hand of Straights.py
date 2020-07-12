"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""846. Hand of Straights
"""

from collections import Counter

class Solution:

    def isNStraightHand(self, hand, W):
        count = Counter(hand)
        keys = sorted(count)
        for i in keys:
            if count[i] > 0:
                freq = count[i]
                for j in range(i, i+W):
                    if count[j] < freq:
                        return False
                    count[j] -= freq
        return True