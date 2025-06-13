from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        paths=[]
        def fs(currPath):
            lastNode=currPath[-1]
            if lastNode==n-1:
                paths.append(currPath)
                return
            if len(currPath)>n: return
            for i in range(len(graph[lastNode])):
                fs(currPath+[graph[lastNode][i]])

        for i in range(len(graph[0])):
            fs([0, graph[0][i]])
        return paths
    
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        def dfs(currPath):
            lastNode = currPath[-1]
            if lastNode == n - 1:
                paths.append(currPath)
                return
            for neighbor in graph[lastNode]:
                dfs(currPath + [neighbor])
        dfs([0])
        return paths