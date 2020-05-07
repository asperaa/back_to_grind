"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""Find the element having minimum absolute difference with target element.
"""

def min_diff_element(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if right == len(nums) - 1:
        return nums[right]
    if abs(nums[right] - target) < abs(nums[left] - target):
        return nums[right]
    else:
        return nums[left]

if __name__ == "__main__":
    nums = [4, 5, 6, 12]
    print(min_diff_element(nums, 12))