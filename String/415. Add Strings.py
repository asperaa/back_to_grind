"""We are the captains ofo ur ships, and we stay 'till the end. We see our stories through.
"""

"""415. Add Strings
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num_1, num_2 = list(num1), list(num2)
        res = []
        carry = 0
        while len(num_1) > 0 or len(num_2) > 0:
            n1 = ord(num_1.pop()) - ord('0') if len(num_1) else 0
            n2 = ord(num_2.pop()) - ord('0') if len(num_2) else 0
            temp = n1 + n2 + carry
            res.append(str(temp % 10))
            carry = temp // 10
        if carry:
            res.append(str(carry))
        return "".join(res)[::-1]
        