
class Solution:
    
    def nextLargerElement(self, arr):
        n = len(arr)
        nge = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if not stack: nge[i] = -1
            if stack and stack[-1] > arr[i]:
                nge[i] = stack[-1]
            stack.append(arr[i])
        return nge