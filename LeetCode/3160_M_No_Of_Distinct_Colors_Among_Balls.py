# from typing import List
# class Solution:
#     def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
#         def distinct(balls):
#             colors=set()
#             for i in range(len(balls)):
#                 if(balls[i]!=0): colors.add(balls[i])
#             return len(colors)

#         balls=[0]*(limit+1)
#         res=[]
#         for i in range(len(queries)):
#             balls[queries[i][0]]=queries[i][1]
#             res.append(distinct(balls))
#         return res
    
# from typing import List
# class Solution:
#     def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
#         lastMax=queries[0][0]
#         res=[1]
#         for i in range(1, len(queries)):
#             if(queries[i][0]>lastMax): lastMax=queries[i][0]
#             res.append(lastMax)
#         return res
    
from typing import List
from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {} 
        colorCount = defaultdict(int) 
        distinctColors = 0 
        res = []
        for pos, color in queries:
            if pos in balls:
                oldColor = balls[pos]
                colorCount[oldColor] -= 1
                if colorCount[oldColor] == 0: distinctColors -= 1
            
            balls[pos] = color 
            if colorCount[color] == 0: distinctColors += 1
            colorCount[color] += 1
            res.append(distinctColors) 
        return res