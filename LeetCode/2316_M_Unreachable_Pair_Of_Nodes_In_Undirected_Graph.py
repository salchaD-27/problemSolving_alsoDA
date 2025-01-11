from typing import List

class Solution:
    def otherNode(self, edge: List[int], key: int) -> int:
        for val in edge:
            if val != key:
                return val

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        component_sizes = []

        def dfs(node):
            stack = [node]
            size = 0
            while stack:
                curr = stack.pop()
                if not visited[curr]:
                    visited[curr] = True
                    size += 1
                    for neighbor in graph[curr]:
                        if not visited[neighbor]: stack.append(neighbor)
            return size

        for node in range(n):
            if not visited[node]:
                component_sizes.append(dfs(node))
        total_pairs = n * (n - 1) // 2
        reachable_pairs = 0
        for size in component_sizes:
            reachable_pairs += size * (size - 1) // 2
        return total_pairs - reachable_pairs