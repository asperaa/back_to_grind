"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""93. Restore IP Addresses
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        self.helper(s, "", 0)
        return self.ans

    def helper(self, s, curr_s, count):
        if count == 4:
            if not s:
                self.ans.append(curr_s[:-1])
        else:
            for i in range(1, 4):
                if i <= len(s):
                    if i == 1:
                        self.helper(s[i:], curr_s + s[:i] + ".", count + 1)
                    elif i == 2 and s[0] != "0":
                        self.helper(s[i:], curr_s + s[:i] + ".", count + 1)
                    elif i == 3 and s[0] != "0" and int(s[:i]) <= 255:
                        self.helper(s[i:], curr_s + s[:i] + ".", count + 1)
                 