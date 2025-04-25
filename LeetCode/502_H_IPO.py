import heapq
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort()
        max_heap = []
        idx = 0
        for _ in range(k):
            while idx < len(projects) and projects[idx][0] <= w:
                heapq.heappush(max_heap, -projects[idx][1])
                idx += 1
            if max_heap: w -= heapq.heappop(max_heap)
            else: break
        return w