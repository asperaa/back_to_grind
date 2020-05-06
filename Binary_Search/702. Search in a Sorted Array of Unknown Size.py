"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""702. Search in a Sorted Array of Unknown Size
"""

class Solution:

    def search(self, reader, target):
        temp_left, temp_right = self.first_big_int(reader)
        right_boundery = self.get_right_boundry(reader, temp_left, temp_right)
        return self.binary_search(reader, target, right_boundery)

    def first_big_int(self, reader):
        left, right = 0, 1
        while reader.get(right) != 2147483647:
            left = right
            right = 2*right
        return (left, right)
    
    def get_right_boundry(self, reader, left, right):
        right_boundry = right
        target = 2147483647
        while left <= right:
            mid = left + (right-left) // 2
            if reader.get(mid) == target:
                right_boundry = mid
                right = mid - 1
            elif reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        return right_boundry
    
    def binary_search(self, reader, target, right_boundry):
        left, right = 0, right_boundry - 1
        while left <= right:
            mid = left + (right - left) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
