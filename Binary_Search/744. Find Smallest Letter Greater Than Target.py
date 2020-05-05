"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""744. Find Smallest Letter Greater Than Target
"""

class Solution:

    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1
        next_great_letter = letters[0]
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] == target:
                left = mid + 1
            elif letters[mid] > target:
                next_great_letter = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        if left == len(letters) and letters[left-1] < target:
            return letters[0]
        return next_great_letter