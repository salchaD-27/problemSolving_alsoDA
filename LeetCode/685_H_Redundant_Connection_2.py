# from typing import List
# class Solution:
#     def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
#         nodes=set()
#         for i in range(len(edges)):
#             nodes.add(edges[i][0])
#             nodes.add(edges[i][1])
#         parentOfSomebody=[False]*(len(nodes)+1)
#         edgeTo=[False]*(len(nodes)+1)
#         for i in range(len(edges)):
#             if parentOfSomebody[edges[i][1]]==False and edgeTo[edges[i][1]]==False:
#                 parentOfSomebody[edges[i][0]]=True
#                 edgeTo[edges[i][1]]=True
#             elif parentOfSomebody[edges[i][1]]==False and edgeTo[edges[i][1]]==True: return edges[i]
#             elif parentOfSomebody[edges[i][1]]==True and edgeTo[edges[i][1]]==False: return edges[i]
        
from typing import List
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0] * (n + 1)
        cand1 = []
        cand2 = []
        for u, v in edges:
            if parent[v] == 0: parent[v] = u
            else:
                cand1 = [parent[v], v]
                cand2 = [u, v]
                break
        def find(uf, x):
            if uf[x] != x: uf[x] = find(uf, uf[x])
            return uf[x]
        uf = list(range(n + 1))
        for u, v in edges:
            if [u, v] == cand2: continue
            pu = find(uf, u)
            pv = find(uf, v)
            if pu == pv:
                # cycle
                if cand1: return cand1
                return [u, v]
            uf[pv] = pu
        # no cycle
        return cand2