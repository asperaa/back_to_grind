# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
        q = deque()
        q.append((src, 0))
        min_cost = [float('inf') for i in range(n)]
        stops = 0

        while q and stops <= k:
            size = len(q)
            for i in range(size):
                curr_node, cost = q.popleft()
                for neighbour, price in graph[curr_node]:
                    if price + cost >= min_cost[neighbour]:
                        continue
                    min_cost[neighbour] = price + cost
                    q.append((neighbour, min_cost[neighbour]))
            stops += 1

        return -1 if min_cost[dst] == float('inf') else min_cost[dst]