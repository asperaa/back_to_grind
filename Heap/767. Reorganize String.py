"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""767. Reorganize String
"""

from heapq import heapify, heappop, heappush

class Solution:

    def reorganizeString(self, S):
        hash_map = {}
        for c in S:
            hash_map[c] = hash_map.get(c, 0) + 1
        max_heap = [(-1* freq, char) for char, freq in hash_map.items()]
        heapify(max_heap)
        reorganized_list = []
        while len(max_heap) > 1:
            first_freq, first_char = heappop(max_heap)
            second_freq, second_char = heappop(max_heap)
            if first_freq != second_freq:
                remaining_first_chars = (-1 * first_freq) - (-1 * second_freq)
                heappush(max_heap, (-1 * remaining_first_chars, first_char))
            second_freq = -1 * second_freq
            while second_freq:
                reorganized_list.append(first_char + second_char)
                second_freq -= 1
        if max_heap:
            if abs(max_heap[0][0]) == 1:
                reorganized_list.append(max_heap[0][1])
                return "".join(reorganized_list)
            return ""
        return "".join(reorganized_list)

