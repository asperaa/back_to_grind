"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes/0
"""

from heapq import heappop, heappush,heapify

def connect_with_min_cost(lengths):
    min_heap = [length for length in lengths]
    heapify(min_heap)
    cost = 0
    while len(min_heap) > 1:
        first_rope = heappop(min_heap)
        second_rope = heappop(min_heap)
        cost += first_rope + second_rope
        heappush(min_heap, first_rope + second_rope)
    return cost

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        lengths = [int(i) for i in input().split()]
        print(connect_with_min_cost(lengths))
        t -= 1