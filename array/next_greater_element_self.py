"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

def next_greater_element(arr):
    stack = []
    length = len(arr)
    result = [None]*length
    result[length-1] = 0
    for i in range(length - 2, -1, -1):
        if arr[i] < arr[i+1]:
            stack.append(arr[i+1])
        else:
            while stack and arr[i] >= stack[-1]:
                stack.pop()
        result[i] = stack[-1] if stack else 0
    return result

if __name__ == "__main__":
    arr = [5, 2, 5]
    print(next_greater_element(arr))

