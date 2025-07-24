# from typing import List
# from collections import defaultdict
# class Solution:
#     def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
#         n = len(nums)
#         tree = defaultdict(list)
#         for u, v in edges:
#             tree[u].append(v)
#             tree[v].append(u)
#         xor = [0] * n
#         parent = [-1] * n

#         # dfs to compute xor of subtree rooted at each node
#         def dfs(node: int, par: int):
#             xor[node] = nums[node]
#             parent[node] = par
#             for nei in tree[node]:
#                 if nei != par:
#                     dfs(nei, node)
#                     xor[node] ^= xor[nei]
#         dfs(0, -1)
#         total = xor[0]  # xor of entire tree
#         min_score = float('inf') # all pairs of nodes
#         for i in range(n):
#             for j in range(i + 1, n):
#                 a, b = i, j
#                 def is_ancestor(u, v):
#                     while v != -1:
#                         if u == v: return True
#                         v = parent[v]
#                     return False
#                 if is_ancestor(a, b):
#                     xor1 = xor[b]
#                     xor2 = xor[a] ^ xor[b]
#                     xor3 = total ^ xor[a]
#                 elif is_ancestor(b, a):
#                     xor1 = xor[a]
#                     xor2 = xor[b] ^ xor[a]
#                     xor3 = total ^ xor[b]
#                 else:
#                     xor1 = xor[a]
#                     xor2 = xor[b]
#                     xor3 = total ^ xor[a] ^ xor[b]
#                 max_x = max(xor1, xor2, xor3)
#                 min_x = min(xor1, xor2, xor3)
#                 min_score = min(min_score, max_x - min_x)
#         return min_score

import collections
from typing import List
class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        subtree_xor = [0] * n
        descendants = [set() for _ in range(n)]

        def dfs(node, parent):
            subtree_xor[node] = nums[node]
            descendants[node].add(node)
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    subtree_xor[node] ^= subtree_xor[neighbor]
                    descendants[node].update(descendants[neighbor])

        dfs(0, -1)
        total_xor = subtree_xor[0]
        min_score = float('inf')
        for i in range(1, n):
            for j in range(i + 1, n):
                xor_i = subtree_xor[i]
                xor_j = subtree_xor[j]
                if j in descendants[i]:
                    val1 = xor_j
                    val2 = xor_i ^ xor_j
                    val3 = total_xor ^ xor_i
                elif i in descendants[j]:
                    val1 = xor_i
                    val2 = xor_j ^ xor_i
                    val3 = total_xor ^ xor_j
                else:
                    val1 = xor_i
                    val2 = xor_j
                    val3 = total_xor ^ xor_i ^ xor_j
                score = max(val1, val2, val3) - min(val1, val2, val3)
                min_score = min(min_score, score)
        return min_score