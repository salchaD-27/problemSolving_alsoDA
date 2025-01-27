# from typing import List
# class Solution:
#     def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         if not prerequisites: return [False] * len(queries)
#         course = [[] for _ in range(numCourses)]
#         for pre in prerequisites:
#             course[pre[1]].append(pre[0])
#         for i in range(numCourses):
#             for prereq in course[i]:
#                 course[i].extend(course[prereq])
#             course[i] = list(set(course[i]))
#         ans = []
#         for query in queries:
#             if query[0] in course[query[1]]: ans.append(True)
#             else: ans.append(False)
#         return ans

from typing import List
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            reachable[u][v] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]: reachable[i][j] = True
        return [reachable[u][v] for u, v in queries]