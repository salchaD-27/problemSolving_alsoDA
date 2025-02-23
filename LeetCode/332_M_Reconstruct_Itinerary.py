# from typing import List
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         res=['JFK']
#         lastStation=res[-1]
#         while(tickets):
#             temp=[]
#             for [a,b] in tickets:
#                 if(a==lastStation): temp.append(b)
#             temp.sort()
#             if(not temp): break
#             res.append(temp[0])
#             tickets.remove([lastStation,temp[0]])
#             lastStation=res[-1]

from typing import List
from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(node):
            while graph[node]:
                dfs(heapq.heappop(graph[node]))
            res.append(node)

        graph = defaultdict(list)
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)
        res = []
        dfs("JFK")
        return res[::-1]