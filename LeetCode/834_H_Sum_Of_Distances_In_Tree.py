# from typing import List
# from collections import deque, defaultdict
# class Solution:
#     def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
#         graph = defaultdict(list)
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
        
#         def bfs(start):
#             visited = [False] * n
#             queue = deque([(start, 0)])
#             visited[start] = True
#             total = 0
#             while queue:
#                 node, dist = queue.popleft()
#                 total += dist
#                 for neighbor in graph[node]:
#                     if not visited[neighbor]:
#                         visited[neighbor] = True
#                         queue.append((neighbor, dist + 1))
#             return total
        
#         res = [bfs(i) for i in range(n)]
#         return res

import collections
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)

        dfs(0, -1)
        dfs2(0, -1)
        return res