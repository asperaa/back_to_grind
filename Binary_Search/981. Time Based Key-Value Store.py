"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""981. Time Based Key-Value Store
"""

class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].append((value, timestamp))
        else:
            self.hash_map[key] = [(value, timestamp)]

        

    def get(self, key: str, timestamp: int) -> str:
        ans = self.binary_search(self.hash_map[key], timestamp)
        return ans

    def binary_search(self, values, timestamp):
        left, right = 0, len(values) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                result = left
                left = mid + 1
            else:
                right = mid - 1
        if result == -1:
            return ""
        return values[result][0]
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)