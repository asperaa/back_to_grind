"""We are the captains ouf our ships, and we stay 'till the end. We see our stories through.
"""

"""https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/
"""

def binary_search(nums, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def search_infinite(nums, target):
    left, right = 0, 1
    while nums[right] < target:
        left = right
        right = 2 * right
    return binary_search(nums, left, right, target)

if __name__ == "__main__":
    nums = [1, 3]
    print(search_infinite(nums, 1))