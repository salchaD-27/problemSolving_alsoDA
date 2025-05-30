import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        heap = [(0, k)]
        visited = {}
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited: continue
            visited[node] = time
            for neighbor, wt in graph[node]:
                if neighbor not in visited: heapq.heappush(heap, (time + wt, neighbor))
        if len(visited) != n: return -1
        return max(visited.values())