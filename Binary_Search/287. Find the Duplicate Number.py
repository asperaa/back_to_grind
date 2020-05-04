"""We are the captains of our ships, and we stay 'till the end. We see ourstories through.
"""

"""287. Find the Duplicate Number
"""

class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow