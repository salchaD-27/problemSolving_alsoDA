# from typing import List
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         completed=[]
#         courses=[i for i in range(numCourses)]
#         for course in courses:
#             for pre in prerequisites:
#                 if(pre[0]==course and pre[1] not in completed): return False
#                 else: completed.append(course)
#         return True

from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            if course in visited: return False
            if not graph[course]: return True
            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre): return False
            visited.remove(course)
            graph[course] = []
            return True
        
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        visited = set()
        for course in range(numCourses):
            if not dfs(course): return False
        return True