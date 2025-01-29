# from typing import List
# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = []
#     def addEdge(self, u, v, w):
#         self.graph.append([u, v, w])
#     def find(self, parent, i):
#         parent[i] = self.find(parent, parent[i])
#         return parent[i]
#     def union(self, parent, rank, x, y):
#         if rank[x] < rank[y]: parent[x] = y
#         elif rank[x] > rank[y]: parent[y] = x
#         else:
#             parent[y] = x
#             rank[x] += 1
#     def KruskalMST(self):
#         result = []
#         i = 0
#         e = 0
#         self.graph = sorted(self.graph, key=lambda item: item[2])
#         parent = []
#         rank = []
#         for node in range(self.V):
#             parent.append(node)
#             rank.append(0)
#         while e < self.V - 1:
#             u, v, w = self.graph[i]
#             i = i + 1
#             x = self.find(parent, u)
#             y = self.find(parent, v)
#             if x != y:
#                 e = e + 1
#                 result.append([u, v, w])
#                 self.union(parent, rank, x, y)
#         return result

# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         g = Graph(len(edges))
#         for i in range(len(edges)):
#             g.addEdge(edges[i][0]-1, edges[i][1]-1, i)
#         res = g.KruskalMST()
#         nonRedEdges=[]
#         for i in range(len(res)):
#             nonRedEdges.append([edges[i][0]+1, edges[i][1]+1])
#         redEdges=[]
#         for edge in edges:
#             if edge not in nonRedEdges: redEdges.append(edge)
#         return redEdges[-1]

from typing import List
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, i):
        if self.parent[i] != i: self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU == rootV: return False
        if self.rank[rootU] > self.rank[rootV]: self.parent[rootV] = rootU
        elif self.rank[rootU] < self.rank[rootV]: self.parent[rootU] = rootV
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u - 1, v - 1): return [u, v]