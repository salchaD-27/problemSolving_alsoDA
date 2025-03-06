from typing import List
from collections import defaultdict
class Graph:
    def __init__(self, equations: List[List[str]], values: List[float]):
        self.graph = defaultdict(list)
        for (u, v), weight in zip(equations, values):
            self.graph[u].append((v, weight))  
            self.graph[v].append((u, 1.0 / weight))  
    def dfs(self, node: str, target: str, visited: set, dist: float) -> float:
        if node not in self.graph or target not in self.graph: return -1.0 
        if node == target: return dist 
        visited.add(node)
        for neighbor, weight in self.graph[node]:
            if neighbor not in visited:
                result = self.dfs(neighbor, target, visited, dist * weight)
                if result != -1: return result
        return -1.0 
    def find_distance(self, start: str, end: str) -> float:
        if start not in self.graph or end not in self.graph: return -1.0 
        return self.dfs(start, end, set(), 1.0)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = Graph(equations, values) 
        return [g.find_distance(query[0], query[1]) for query in queries]