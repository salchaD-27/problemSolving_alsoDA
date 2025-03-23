import heapq
from typing import List
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adj = [[] for _ in range(n)]
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))
        # Dijkstra's
        dist = [float('inf')] * n  
        ways = [0] * n  
        dist[0] = 0
        ways[0] = 1  
        # Min-heap priority queue
        pq = [(0, 0)]
        while pq:
            curr_time, u = heapq.heappop(pq)
            if curr_time > dist[u]: continue
            for v, time in adj[u]:
                new_time = curr_time + time
                if new_time < dist[v]:
                    dist[v] = new_time
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_time, v))
                elif new_time == dist[v]: ways[v] = (ways[v] + ways[u]) % MOD
        return ways[n-1]