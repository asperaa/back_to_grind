"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""451. Sort Characters By Frequency
"""


from heapq import heapify, heappop, heappush

class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = {}
        for c in s:
            hash_map[c] = hash_map.get(c, 0) + 1
        max_heap = []
        heapify(max_heap)
        for char, freq in hash_map.items():
            heappush(max_heap, (-1*freq, char))
        result = ""
        while len(max_heap) > 0:
            freq, char = heappop(max_heap)
            freq = -1 * freq
            result += char*freq 
        return result
