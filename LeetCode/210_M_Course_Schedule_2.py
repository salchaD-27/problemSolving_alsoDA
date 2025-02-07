# from typing import List
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         def loop(res, c1, c2):
#             indexC1=0
#             indexC2=0
#             for i in range(len(res)):
#                 if(res[i]==c1): indexC1=i
#                 if(res[i]==c2): indexC2=i
#             return indexC2>indexC1

#         if(not prerequisites): return [i for i in range(numCourses)]
#         res=[]
#         for i in range(len(prerequisites)):
#             if((prerequisites[i][0] in res) and (prerequisites[i][1] in res) and (loop(res, prerequisites[i][0], prerequisites[i][1]))):
#                 return []
#             elif((prerequisites[i][0] not in res) and (prerequisites[i][1] not in res)):
#                 res.append(prerequisites[i][1])
#                 res.append(prerequisites[i][0])
#             elif((prerequisites[i][0] not in res) and (prerequisites[i][1] in res)):
#                 res.append(prerequisites[i][0])
#             elif((prerequisites[i][0] in res) and (prerequisites[i][1] not in res)):
#                 res.insert(res.index(prerequisites[i][0]), prerequisites[i][1])
        
#         if(len(res)<numCourses): 
#             ref=[i for i in range(numCourses)]
#             for num in ref:
#                 if num not in res:
#                     res.append(num)
#         return res

# from typing import List
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         def loop(res, c1, c2):
#             if c1 in res and c2 in res:
#                 indexC1 = res.index(c1)
#                 indexC2 = res.index(c2)
#                 return indexC1 < indexC2
#             return False

#         if not prerequisites: return [i for i in range(numCourses)]
#         res = []
#         for c1, c2 in prerequisites:
#             if (c1 in res and c2 in res and loop(res, c1, c2)): return []
#             elif c1 not in res and c2 not in res:
#                 res.append(c2)
#                 res.append(c1)
#             elif c1 not in res and c2 in res:
#                 res.append(c1)
#             elif c1 in res and c2 not in res:
#                 res.insert(res.index(c1), c2)
#         for i in range(numCourses):
#             if i not in res: res.append(i)
#         return res

from typing import List
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1   
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for dependent in graph[course]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0: queue.append(dependent)
        return order if len(order) == numCourses else []