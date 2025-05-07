# from typing import List
# class Solution:
#     def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
#         minX = minY = float('inf')
#         maxX = maxY = float('-inf')
#         minXIdx = minYIdx = maxXIdx = maxYIdx = 0
#         for i in range(len(trees)):
#             if trees[i][0] < minX: 
#                 minX = trees[i][0]
#                 minXIdx = i
#             if trees[i][1] < minY: 
#                 minY = trees[i][1]
#                 minYIdx = i
#             if trees[i][0] > maxX: 
#                 maxX = trees[i][0]
#                 maxXIdx = i
#             if trees[i][1] > maxY: 
#                 maxY = trees[i][1]
#                 maxYIdx = i
#         res = [trees[minXIdx], trees[minYIdx], trees[maxXIdx], trees[maxYIdx]]

#         def orientation(p, q, r): return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
#         def is_on_boundary(p):
#             return (orientation(trees[minXIdx], trees[minYIdx], p) >= 0 and
#                     orientation(trees[minYIdx], trees[maxXIdx], p) >= 0 and
#                     orientation(trees[maxXIdx], trees[maxYIdx], p) >= 0 and
#                     orientation(trees[maxYIdx], trees[minXIdx], p) >= 0)
        
#         for tree in trees:
#             if tree not in res and is_on_boundary(tree): res.append(tree)
#         return res

# from typing import List
# class Solution:
#     def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
#         def cross(o, a, b):  return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

#         trees.sort()
#         lower = []
#         for tree in trees:
#             while len(lower) >= 2 and cross(lower[-2], lower[-1], tree) <= 0:
#                 lower.pop()
#             lower.append(tree)
#         upper = []
#         for tree in reversed(trees):
#             while len(upper) >= 2 and cross(upper[-2], upper[-1], tree) <= 0:
#                 upper.pop()
#             upper.append(tree)
#         result = lower[:-1] + upper[:-1]
#         seen = set()
#         final_result = []
#         for point in result:
#             if tuple(point) not in seen:
#                 final_result.append(point)
#                 seen.add(tuple(point))
#         return final_result

from typing import List
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        def crossProduct(p1,p2,p3):
            ### V1 = (a,b), V2 = (c,d)
            ### V1 X V2 = a*d - b*c
            ### V1 = (P2,P3)
            ### V2 = (P1,P2)
            a = p3[0]-p2[0]
            b = p3[1]-p2[1]
            c = p2[0]-p1[0]
            d = p2[1]-p1[1]
            return  a*d - b*c
        
        def constructHalfHull(points):
            stack = []
            for p in points:
                while len(stack)>=2 and crossProduct(stack[-2],stack[-1],p)>0:
                    stack.pop()
                stack.append(tuple(p))
            return stack
        
        points.sort()
        leftToRight = constructHalfHull(points)
        rightToLeft = constructHalfHull(points[::-1])
        return list(set(leftToRight + rightToLeft))