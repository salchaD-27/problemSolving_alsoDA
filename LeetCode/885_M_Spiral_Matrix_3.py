# from typing import List
# class Solution:
#     def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
#         n=rows*cols
#         res=[[rStart,cStart]]
#         lastE,lastS=0,0
#         nextMove={'N':'E','E':'S','S':'W','W':'N'}
#         lastMoved='N'
#         dir={'N':[-1,0],'E':[0,1],'W':[0,-1],'S':[1,0]}
#         while(len(res)<n):
#             toMove=nextMove[lastMoved]
#             if toMove=='N':
#                 movement=lastS+1
#                 rStart+=movement*dir[toMove][0]
#                 cStart+=movement*dir[toMove][1]
#             elif toMove=='E':
#                 movement=lastE+1
#                 rStart+=movement*dir[toMove][0]
#                 cStart+=movement*dir[toMove][1]
#                 lastE+=1
#             elif toMove=='W':
#                 movement=lastE+1
#                 rStart+=movement*dir[toMove][0]
#                 cStart+=movement*dir[toMove][1]
#             elif toMove=='S':
#                 movement=lastS+1
#                 rStart+=movement*dir[toMove][0]
#                 cStart+=movement*dir[toMove][1]
#                 lastS+=1
#             if 0<=rStart<rows and 0<=cStart<cols: res.append([rStart,cStart])
#         return res

from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        total = rows * cols
        x, y = rStart, cStart
        steps = 1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # E, S, W, N
        d = 0
        while len(res) < total:
            for _ in range(2):
                dx, dy = dirs[d % 4]
                for _ in range(steps):
                    if 0 <= x < rows and 0 <= y < cols: res.append([x, y])
                    x += dx
                    y += dy
                d += 1
            steps += 1
        return res