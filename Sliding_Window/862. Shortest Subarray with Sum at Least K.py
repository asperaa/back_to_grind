"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""862. Shortest Subarray with Sum at Least K
"""

from collections import deque

class Solution:

    def shortestSubarray(self, nums, k):
        n = len(nums)
        ans = n+1
        pre_sum = [0 for _ in range(n+1)]
        start_queue = deque()
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]
        for end in range(n+1):
            while start_queue and pre_sum[end] - pre_sum[start_queue[0]] >= k:
                start = start_queue.popleft()
                ans = min(ans, end - start)
            while start_queue and pre_sum[end] <= pre_sum[start_queue[-1]]:
                start_queue.pop()
            start_queue.append(end)
        return ans if ans <= n else -1

        




