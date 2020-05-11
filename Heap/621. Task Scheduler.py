"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""621. Task Scheduler
"""

from heapq import heappop, heappush, heapify

class Solution:

    def leastInterval(self, tasks, n):
        hash_map = {}
        for task in tasks:
            hash_map[task] = hash_map.get(task, 0) + 1
        max_heap = [-1 * freq for task, freq in hash_map.items()]
        heapify(max_heap)
        all_times = 0
        cycle = n + 1
        print("HI")
        while len(max_heap) > 0:
            times = 0
            temp_freq = []
            for i in range(cycle):
                if not max_heap:
                    break
                temp_freq.append(-1*heappop(max_heap))
                times += 1
            for freq in temp_freq:
                if freq-1:
                    heappush(max_heap, -1 * (freq-1))
            all_times += cycle if max_heap else times
        return all_times 

if __name__ == "__main__":
    s = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    print(s.leastInterval(tasks, 2))
