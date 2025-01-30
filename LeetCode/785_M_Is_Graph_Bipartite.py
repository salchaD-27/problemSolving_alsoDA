from collections import deque
from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs_check_bipartite(start):
            queue = deque([start])
            colors[start] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in colors:
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]: return False
            return True
        
        colors = {}
        for node in range(len(graph)): 
            if node not in colors: 
                if not bfs_check_bipartite(node): return False 
        return True