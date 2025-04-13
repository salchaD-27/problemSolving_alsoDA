# [[3,4],[2,3],[1,2]]
# intrvl:origIndx (O(n))
# [1]:2
# [2]:1
# [3]:0

# sorted=[[1,2],[2,3],[3,4]]
# intrvl:rightIndx (O(n))
# [1,2]:1
# [2,3]:0
# [3,4]:-1

# from typing import List
# class Solution:
#     def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
#         if(len(intervals)<2): return [-1]
#         origIndxMap={}
#         for i in range(len(intervals)):
#             origIndxMap[intervals[i][0]]=i
#         rightIndx={}
#         intervals.sort()
#         for i in range(len(intervals)-1):
#             if(intervals[i][1]<=intervals[i+1][0]):
#                 rightIndx[intervals[i][0]]=origIndxMap[intervals[i+1][0]]
#             else:
#                 rightIndx[intervals[i][0]]=-1
#         res=[]
#         for i in range(len(intervals)):
#             res.append(rightIndx[intervals[i][0]])
#         return res

# from typing import List
# class Solution:
#     def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
#         if len(intervals) < 2: return [-1]
#         origIndxMap = {interval[0]: i for i, interval in enumerate(intervals)}
#         rightIndx = {}
#         intervals.sort()
#         for i in range(len(intervals) - 1):
#             if intervals[i][1] <= intervals[i+1][0]: rightIndx[intervals[i][0]] = origIndxMap[intervals[i+1][0]]
#             else: rightIndx[intervals[i][0]] = -1
#         last_start = intervals[-1][0]
#         rightIndx[last_start] = -1
#         res = []
#         for interval in intervals:
#             key = interval[0]
#             res.append(rightIndx.get(key, -1))
#         final_res = [0] * len(intervals)
#         for start, idx in origIndxMap.items():
#             final_res[idx] = rightIndx.get(start, -1)
#         return final_res

import bisect
from typing import List
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # [start, original_index]
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        res = []
        for interval in intervals:
            end = interval[1]
            idx = bisect.bisect_left(starts, (end,))
            if idx < len(starts): res.append(starts[idx][1])
            else: res.append(-1)
        return res