"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""402. Remove K Digits
"""

class Solution:

    def removeKdigits(self, num, k):
        n = len(num)
        keep = n - k
        ans = []
        for i in range(n):
            while ans and k and ans[-1] > num[i]:
                ans.pop()
                k -= 1
            ans.append(num[i])
        ans = ans[:keep]
        return "".join(ans).lstrip("0") or "0"