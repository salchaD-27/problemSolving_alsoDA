# 1. Find the shortest bob's path via bfs/dfs from bob's node to node 0
# 2. Find the optimal path for alice such that considering amounts that bob's path will coincide and thus change those nodes' values respectively
# 3. On getting path of both bob and alice, iterate over the path and add the values of the nodes in the path to get the total amount

from typing import List
from collections import deque, defaultdict
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # BFS for Bob's shortest path
        parent = {0: None}
        queue = deque([0])
        depth_bob = {}
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in parent:
                    parent[neighbor] = node
                    queue.append(neighbor)
        curr, d = bob, 0
        while curr is not None:
            depth_bob[curr] = d
            curr = parent[curr]
            d += 1
        
        def dfs(node, depth, prev):
            alice_depth[node] = depth
            for neighbor in graph[node]:
                if neighbor != prev:
                    dfs(neighbor, depth + 1, node)
        alice_depth = {}
        dfs(0, 0, -1)
        
        def dfs_alice(node, prev, curr_profit):
            nonlocal max_profit
            is_leaf = True
            curr_profit += amount[node]
            for neighbor in graph[node]:
                if neighbor != prev:
                    is_leaf = False
                    dfs_alice(neighbor, node, curr_profit)
            if is_leaf: max_profit = max(max_profit, curr_profit)
        for node in depth_bob:
            if alice_depth[node] < depth_bob[node]: pass
            elif alice_depth[node] == depth_bob[node]: amount[node] //= 2
            else: amount[node] = 0
        max_profit = float('-inf')
        
        dfs_alice(0, -1, 0)
        return max_profit