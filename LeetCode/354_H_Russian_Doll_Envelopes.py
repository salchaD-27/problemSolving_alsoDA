# from typing import List
# from collections import defaultdict
# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         def longestPath(edges):
#             def dfs(node):
#                 if node in memo: return memo[node]
#                 max_length = 0
#                 for neighbor in graph[node]:
#                     max_length = max(max_length, dfs(neighbor) + 1)
#                 memo[node] = max_length
#                 return max_length
            
#             graph = defaultdict(list)
#             for u, v in edges:
#                 graph[u].append(v)
#             memo = {}
#             longest = 0
#             for node in list(graph.keys()):
#                 longest = max(longest, dfs(node))
#             return longest 
        
#         edges=[]
#         for i in range(len(envelopes)):
#             for j in range(len(envelopes)):
#                 if(i!=j):
#                     if(envelopes[i][0]<envelopes[j][0] and envelopes[i][1]<envelopes[j][1]): edges.append([i,j])
#         return max(1, longestPath(edges)+1)
    
from typing import List
import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []  
        for _, height in envelopes:
            idx = bisect.bisect_left(lis, height)
            if idx == len(lis): lis.append(height)
            else: lis[idx] = height
        return len(lis)