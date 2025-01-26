# def dfs_rec(adj, visited, s):
#     visited[s] = True
#     print(s, end=" ")
#     for i in adj[s]:
#         if not visited[i]:
#             dfs_rec(adj, visited, i)
# def dfs(adj, s):
#     visited = [False] * len(adj)
#     dfs_rec(adj, visited, s)
# def add_edge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)

# V = 5
# adj = [[] for _ in range(V)]
# edges = [[0, 1], [1, 2], [2, 0]]
# # [2,2,1,2]
# # [1,2,0]
# # [3,0,1,4,1]
# for e in edges:
#     add_edge(adj, e[0], e[1])
# for source in edges:
#     dfs(adj, source[0])

# from typing import List
# from collections import defaultdict
# class Solution:
#     def maximumInvitations(self, favorite: List[int]) -> int:
#         def dfs(node, favorite, visited, stack, stack_index):
#             if visited[node]:
#                 if node in stack_index: return len(stack) - stack_index[node], 0
#                 else: return 0, 0
#             visited[node] = True
#             stack_index[node] = len(stack)
#             stack.append(node)
#             cycle_length, chain_length = dfs(favorite[node], favorite, visited, stack, stack_index)
#             stack.pop()
#             del stack_index[node]
#             return cycle_length, chain_length + 1 if cycle_length == 0 else 0

#         n = len(favorite)
#         visited = [False] * n
#         max_cycle_length = 0
#         chain_lengths = defaultdict(int)
#         for i in range(n):
#             if not visited[i]:
#                 stack = []
#                 stack_index = {}
#                 cycle_length, chain_length = dfs(i, favorite, visited, stack, stack_index)

#                 if cycle_length > 0: max_cycle_length = max(max_cycle_length, cycle_length)
#                 else: chain_lengths[i] = max(chain_lengths[i], chain_length)
#         mutual_favorite_chain_sum = 0
#         for i in range(n):
#             j = favorite[i]
#             if favorite[j] == i and i < j: mutual_favorite_chain_sum += 2 + chain_lengths[i] + chain_lengths[j]
#         return max(max_cycle_length, mutual_favorite_chain_sum)

from typing import List
from collections import defaultdict, deque
class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)
        visited = [False] * n
        in_degree = [0] * n
        for i in range(n):
            in_degree[favorite[i]] += 1
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        chain_length = [0] * n
        while queue:
            node = queue.popleft()
            next_node = favorite[node]
            chain_length[next_node] = max(chain_length[next_node], chain_length[node] + 1)
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)
        visited = [False] * n
        max_cycle_length = 0
        mutual_chain_sum = 0
        for i in range(n):
            if not visited[i]:
                cycle_nodes = []
                node = i
                while not visited[node]:
                    visited[node] = True
                    cycle_nodes.append(node)
                    node = favorite[node]
                
                if node in cycle_nodes:
                    cycle_start = cycle_nodes.index(node)
                    cycle_length = len(cycle_nodes) - cycle_start
                    if cycle_length == 2:
                        a, b = cycle_nodes[cycle_start], cycle_nodes[cycle_start + 1]
                        mutual_chain_sum += 2 + chain_length[a] + chain_length[b]
                    else: max_cycle_length = max(max_cycle_length, cycle_length)
        return max(max_cycle_length, mutual_chain_sum)