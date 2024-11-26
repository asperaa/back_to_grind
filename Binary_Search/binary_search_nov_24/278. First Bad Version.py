# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        first_bad_version = -1

        while left <= right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                first_bad_version = mid
                right = mid - 1
            elif not isBadVersion(mid):
                left = mid + 1
        return first_bad_version
        