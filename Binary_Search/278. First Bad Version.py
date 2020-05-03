"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""278. First Bad Version
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        first_bad_version = -1
        while left <= right:
            mid = left + (right-left) // 2
            if isBadVersion(mid) == True:
                first_bad_version = mid
                right = mid - 1
            else:
                left = mid + 1
        return first_bad_version
    
    def isBadVersion(self, n):
        pass