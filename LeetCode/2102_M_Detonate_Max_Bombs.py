from typing import List

class Solution:
    def inArea(self, src: List[int], target: List[int]) -> bool: return (src[0] - target[0])**2 + (src[1] - target[1])**2 <= src[2]**2

    def dfs(self, graph: List[List[int]], visited: set, node: int) -> int:
        visited.add(node)
        count = 1
        for neighbor in graph[node]:
            if neighbor not in visited: count += self.dfs(graph, visited, neighbor)
        return count

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and self.inArea(bombs[i], bombs[j]): graph[i].append(j)
        
        maxBombsDetonated = 0
        for i in range(n):
            visited = set()
            maxBombsDetonated = max(maxBombsDetonated, self.dfs(graph, visited, i))
        return maxBombsDetonated