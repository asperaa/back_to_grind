"""We are the captains of our ships, and we stay through the end. We see our stories through.
"""

"""1365. How Many Numbers Are Smaller Than the Current Number
"""

class Solution:

    def smallerNumbersThanCurrent(self, nums: List[int]):
        sorted_nums = sorted(nums)
        smaller_count = {}
        for i in range(len(sorted_nums)):
            if sorted_nums[i] in smaller_count:
                continue
            smaller_count[sorted_nums[i]] = i
        answer = [0] * len(sorted_nums)
        for i, num in enumerate(nums):
            answer[i] = smaller_count[num]
        return answer





