"""We ar ethe captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""692. Top K Frequent Words
"""

from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        max_heap = [(-1*freq, word) for word, freq in count.items()]
        heapify(max_heap)
        return [heappop(max_heap)[1] for _ in range(k)]
        