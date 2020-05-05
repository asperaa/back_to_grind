"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""125. Valid Palindrome
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    s = Solution()
    st = "race a car"
    print(s.isPalindrome(st))