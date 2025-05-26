from typing import List
from collections import defaultdict, deque
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # topological sort
        queue = deque([i for i in range(n) if indegree[i] == 0])
        topo_order = []
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0: queue.append(neighbor)
        if len(topo_order) != n: return -1

        dp = [[0] * 26 for _ in range(n)]
        for node in topo_order:
            color_idx = ord(colors[node]) - ord('a')
            dp[node][color_idx] += 1
            for neighbor in graph[node]:
                for c in range(26):
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c])
        return max(max(row) for row in dp)