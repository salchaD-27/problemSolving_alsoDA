from collections import defaultdict
from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            stack = [node]
            component_nodes = []
            component_edges = 0
            while stack:
                curr = stack.pop()
                if visited[curr]: continue
                visited[curr] = True
                component_nodes.append(curr)
                for neighbor in adj[curr]:
                    component_edges += 1
                    if not visited[neighbor]:
                        stack.append(neighbor)
            component_edges //= 2
            return component_nodes, component_edges
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = [False] * n
        complete_components = 0
        for i in range(n):
            if not visited[i]:
                component_nodes, component_edges = dfs(i)
                k = len(component_nodes)
                if component_edges == k * (k - 1) // 2: complete_components += 1
        return complete_components