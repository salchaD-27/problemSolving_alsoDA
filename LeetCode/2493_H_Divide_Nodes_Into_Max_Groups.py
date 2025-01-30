from collections import deque, defaultdict
from typing import List
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # Connected components and ipartiteness
        colors = {}
        components = []

        def bfs_check_bipartite(start):
            queue = deque([start])
            colors[start] = 0
            component = {start}
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in colors:
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                        component.add(neighbor)
                    elif colors[neighbor] == colors[node]: return None
            return component

        def bfs_max_depth(start):
            queue = deque([(start, 1)])
            visited = {start}
            max_depth = 1
            while queue:
                node, depth = queue.popleft()
                max_depth = max(max_depth, depth)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, depth + 1))
            return max_depth
        
        visited = set()
        for node in range(1, n + 1):
            if node not in visited:
                result = bfs_check_bipartite(node)
                if result is None: return -1
                visited.update(result)
                components.append(result)
        max_groups = 0
        for component in components:
            max_depth = 0
            for node in component:
                max_depth = max(max_depth, bfs_max_depth(node))
            max_groups += max_depth
        return max_groups