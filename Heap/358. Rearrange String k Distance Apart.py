"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""358. Rearrange String k Distance Apart
"""

from heapq import heapify, heappop, heappush

class Solution:

    def rearrangeString(self, s, k):
        if k == 0:
            return s
        length = len(s)
        freq_book = {}
        for c in s:
            freq_book[c] = freq_book.get(c, 0) + 1
        max_heap = [(-1 * freq, char) for char, freq in freq_book.items()]
        heapify(max_heap)
        new_arrangement = []
        while len(max_heap) >= k:
            popped_elements = []
            for _ in range(k):
                popped_element = heappop(max_heap)
                new_arrangement.append(popped_element[1])
                popped_elements.append(popped_element)
            for popped_element in popped_elements:
                if popped_element[0] + 1:
                    heappush(max_heap, (popped_element[0] + 1, popped_element[1]))
        while max_heap:
            popped_element = heappop(max_heap)
            if abs(popped_element[0]) > 1:
                return "" 
            new_arrangement.append(popped_element[1])
        return "".join(new_arrangement)
                
