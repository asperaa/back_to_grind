"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/k-largest-elements/0
"""
from heapq import heapify, heappush, heappop

def k_largest(nums, k):
    min_heap = []
    heapify(min_heap)
    for num in nums:
        heappush(min_heap, num)
        if len(min_heap) > k:
            heappop(min_heap)
    return min_heap

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, k = [int(i) for i in input().split()]
        nums = [int(i) for i in input().split()]
        print(k_largest(nums, k))
        t -= 1
