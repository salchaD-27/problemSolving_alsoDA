from collections import deque
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        graph = {i: set() for i in range(n)}
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        leaves = deque([i for i in graph if len(graph[i]) == 1])
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1: leaves.append(neighbor)
        return list(leaves)