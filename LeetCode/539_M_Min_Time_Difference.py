# from typing import List
# class Solution:
#     def findMinDifference(self, timePoints: List[str]) -> int:
#         timePoints.sort(reverse=True)
#         res=float('inf')
#         for i in range(len(timePoints)-1):
#             j=i+1
#             if(timePoints[i]==timePoints[j]): return 0
#             t1=60*int(timePoints[i][:2])+int(timePoints[i][3:])
#             t2L=60*int(timePoints[j][:2])+int(timePoints[j][3:])
#             t2U=t2L+60*24
#             res=min(res, abs(t2L-t1), abs(t2U-t1))
#         return res

from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(t[:2]) * 60 + int(t[3:]) for t in timePoints]
        minutes.sort()
        for i in range(1, len(minutes)):
            if minutes[i] == minutes[i - 1]: return 0
        res = float('inf')
        for i in range(1, len(minutes)):
            res = min(res, minutes[i] - minutes[i - 1])
        res = min(res, (minutes[0] + 1440) - minutes[-1])
        return res