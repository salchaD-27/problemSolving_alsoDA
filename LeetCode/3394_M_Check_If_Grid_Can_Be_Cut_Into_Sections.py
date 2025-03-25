# from typing import List
# class Solution:
#     def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
#         xCuts=[]
#         for i in range(len(rectangles)):
#             xcut=rectangles[i][3]
#             if(len(xCuts)==0): xCuts.append(xcut)
#             elif(xcut>xCuts[-1]):
#                 lastXcut=xCuts[-1]
#                 if(lastXcut>rectangles[i][0]):
#                     xCuts[-1]=xcut
#                 else: xCuts.append(xcut)
#         if(n in len(xCuts)): xCuts.remove(n)
#         if(len(xCuts)>=2): return True        
#         yCuts=[]
#         for i in range(len(rectangles)):
#             ycut=rectangles[i][2]
#             if(len(xCuts)==0): yCuts.append(ycut)
#             elif(xcut>xCuts[-1]):
#                 lastYcut=yCuts[-1]
#                 if(lastYcut>rectangles[i][1]):
#                     yCuts[-1]=ycut
#                 else: yCuts.append(ycut)
#         if(n in len(yCuts)): yCuts.remove(n)
#         if(len(yCuts)>=2): return True
#         return False

from typing import List
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(r[0], r[2]) for r in rectangles]  # (x1, x2)
        y = [(r[1], r[3]) for r in rectangles]  # (y1, y2)
        x.sort()
        y.sort()
        def count_non_overlapping(intervals):
            count = 0
            prev_end = -1
            for start, end in intervals:
                if prev_end <= start:
                    count += 1
                prev_end = max(prev_end, end)
            return count
        return max(count_non_overlapping(x), count_non_overlapping(y)) >= 3