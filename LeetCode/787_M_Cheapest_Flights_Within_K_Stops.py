import heapq
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, price in flights:
            graph[u].append((v, price))
        heap = [(0, src, 0)]
        visited = dict()
        while heap:
            cost, city, stops = heapq.heappop(heap)
            if city == dst: return cost
            if stops > k: continue
            if (city in visited and visited[city] <= stops): continue
            visited[city] = stops
            for nei, price in graph[city]:
                heapq.heappush(heap, (cost + price, nei, stops + 1))
        return -1