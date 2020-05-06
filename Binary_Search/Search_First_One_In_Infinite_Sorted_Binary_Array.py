"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""https://www.geeksforgeeks.org/find-index-first-1-infinite-sorted-array-0s-1s/
"""

def search_first_one(nums):
    left, right = 0, 1
    while nums[right] != 1:
        left = right
        right = 2 * right
    first_one = right
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == 1:
            first_one = mid
            right = mid - 1
        elif nums[mid] == 0:
            left = mid + 1
    return first_one

if __name__ == "__main__":
    nums = [0, 0, 0, 1, 1, 1]
    print(search_first_one(nums))