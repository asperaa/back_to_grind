"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""870. Advantage Shuffle
"""

class Solution:

    def advantageCount(self, A, B):
        n = len(A)
        C = []
        for i in range(n):
            C.append([B[i], i])
        A.sort()
        C.sort()
        ans = [0] * n
        low, high = 0, n-1
        for i in range(n-1, -1, -1):
            if C[i][0] < A[high]:
                ans[C[i][1]] = A[high]
                high -= 1
            else:
                ans[C[i][1]] = A[low]
                low += 1
        return ans