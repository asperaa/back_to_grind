"""We are the captain of our ships, and we stay 'till the end. We see our stories through.
"""

"""763. Partition Labels
"""


class Solution:
    
    def partitionLabels(self, s):
        n = len(s)
        p = [[-1, -1] for _ in range(26)]
        for i in range(n):
            index = ord(s[i]) - ord('a')
            if p[index][0] == -1:
                p[index][0] = i
            p[index][1] = i
        positions = sorted(p)
        ans = []
        start = 0
        for i in range(26):
            if positions[i][0] != -1:
                start = i
                low, high = positions[i][0], positions[i][1]
                break
        for i in range(start+1, 26):
            if positions[i][1] > high:
                if positions[i][0] > high:
                    num_elements = high - low + 1
                    ans.append(num_elements)
                    low, high = positions[i][0], positions[i][1]
                else:
                    high = positions[i][1]
        ans.append(high-low+1)
        return ans


