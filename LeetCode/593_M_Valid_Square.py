# from typing import List
# class Solution:
#     def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
#         def subSquareSolver(p1,p2,p3,p4):
#             # 3 4
#             # 1 2
#             Xdiff12=abs(p1[0]-p2[0])
#             Xdiff34=abs(p3[0]-p4[0])
#             Ydiff13=abs(p1[1]-p3[1])
#             Ydiff24=abs(p2[1]-p4[1])
#             return Xdiff12==Xdiff34==Ydiff13==Ydiff24
        
#         # 3 4
#         # 1 2
#         res1=subSquareSolver(p1,p2,p3,p4)
#         # 2 3
#         # 1 4
#         res2=subSquareSolver(p1,p4,p2,p3)
#         # 4 2
#         # 1 3
#         res3=subSquareSolver(p1,p3,p4,p2)
#         # 3 2
#         # 1 4
#         res4=subSquareSolver(p1,p4,p3,p2)
#         return res1 or res2 or res3 or res4

from typing import List
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist2(a, b): return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        def subSquareSolver(p1, p2, p3, p4):
            side1 = dist2(p1, p2)
            side2 = dist2(p2, p3)
            side3 = dist2(p3, p4)
            side4 = dist2(p4, p1)
            diag1 = dist2(p1, p3)
            diag2 = dist2(p2, p4)
            return (
                side1 > 0 and
                side1 == side2 == side3 == side4 and
                diag1 == diag2
            )

        points = [tuple(p1), tuple(p2), tuple(p3), tuple(p4)]
        if len(set(points)) < 4: return False
        return (
            subSquareSolver(p1, p2, p3, p4) or
            subSquareSolver(p1, p4, p2, p3) or
            subSquareSolver(p1, p3, p4, p2) or
            subSquareSolver(p1, p2, p4, p3)
        )