"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://www.geeksforgeeks.org/find-k-closest-numbers-in-an-unsorted-array/
"""

from heapq import heapify, heappop, heappush

class Solution:

    def findClosestElements(self, nums, k, x):
        max_heap = []
        heapify(max_heap)
        for num in nums:
            distance = abs(num-x)
            heappush(max_heap, (-1*distance, num))
            if len(max_heap) > k:
                heappop(max_heap)
        closest_elements = [actual_num for distance, actual_num in max_heap]
        return closest_elements