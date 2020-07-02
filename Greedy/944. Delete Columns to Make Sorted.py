"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""944. Delete Columns to Make Sorted
"""

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = [1 for a in zip(*A) if list(a) != sorted(a)]
        return len(count)
        