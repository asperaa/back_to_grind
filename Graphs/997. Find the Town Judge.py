"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""997. Find the Town Judge
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_deg = [0 for _ in range(N+1)]
        out_deg = [False for _ in range(N+1)]
        for x, y in trust:
            in_deg[y] += 1
            out_deg[x] = True

        for i in range(1, N+1):
            if in_deg[i] == N-1 and not out_deg[i]:
                return i
        return -1
        