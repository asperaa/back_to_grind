"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""239. Sliding Window Maximum
"""

from collections import deque

class Solution:

    def maxSlidingWindow(self, nums, k):
        queue = deque()
        ans = []
        n = len(nums)
        for i in range(n):
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                ans.append(nums[queue[0]])
        return ans
        
