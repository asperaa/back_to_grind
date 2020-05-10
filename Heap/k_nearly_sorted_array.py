"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0
"""

from heapq import heapify, heappop, heappush

def k_nearly_sorted(nums, k):
    min_heap = []
    heapify(min_heap)
    sorted_arr = []
    for num in nums:
        heappush(min_heap, num)
        if len(min_heap) > k:
            min_element_so_far = heappop(min_heap)
            sorted_arr.append(min_element_so_far)
    for i in range(k):
        min_element_so_far = heappop(min_heap)
        sorted_arr.append(min_element_so_far)
    return sorted_arr

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, k = [int(i) for i in input().split()]
        nums = [int(i) for i in input().split()]
        print(k_nearly_sorted(nums, k))
        t -= 1

