"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""719. Find K-th Smallest Pair Distance [Merge Sorted List Method]
"""

from heapq import heapify, heappop, heappush

class Solution:

    def smallestDistancePair(self, nums, k):
        nums = sorted(nums)
        min_heap = [(nums[i+1]- nums[i], i, i+1) for i in range(len(nums)-1)]
        heapify(min_heap)
        while k and min_heap:
            min_diff, i, j = heappop(min_heap)
            if j + 1 < len(nums):
                heappush(min_heap, (nums[j+1]-nums[i], i, j+1))
            k -= 1
        return min_diff



