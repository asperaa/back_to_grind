"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/kth-smallest-element/0
"""

from heapq import heappop, heappush, heapify

def kth_smallest(nums, k):
    max_heap = []
    heapify(max_heap)
    for num in nums:
        heappush(max_heap, -1*num)
        if len(max_heap) > k:
            heappop(max_heap)
    return max_heap[0] * -1

if __name__ == "__main__":
    nums = [10, 3, 20, 4, 70, 7]
    print(kth_smallest(nums, 3))
