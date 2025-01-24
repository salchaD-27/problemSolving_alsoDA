from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def truePath(graph, node, terminalNode, visited):
            if node in visited: return False
            if node in terminalNode: return True
            visited.add(node)
            for val in graph[node]:
                if not truePath(graph, val, terminalNode, visited): return False
            visited.remove(node)
            terminalNode.add(node)
            return True

        terminalNode = set()
        for i in range(len(graph)):
            if graph[i] == []: terminalNode.add(i)
        ans = []
        for i in range(len(graph)):
            if truePath(graph, i, terminalNode, set()): ans.append(i)
        return sorted(ans)