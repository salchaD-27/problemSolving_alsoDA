# from typing import List
# class Solution:
#     def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
#         lenIntervals=[[interval, interval[1]-interval[0]+1] for interval in intervals]
#         lenIntervals.sort(key=lambda x: x[-1])
#         twoNums=[[]]*len(intervals)
#         contSet=[]
#         for i in range(len(lenIntervals)):
#             if lenIntervals[i][1]==2: twoNums[i]=lenIntervals[i][0]
#             else:
#                 if i!=0 and i!=len(lenIntervals)-1:
#                     prevint=lenIntervals[i-1][0]
#                     interval=lenIntervals[i][0]
#                     nextint=lenIntervals[i+1][0]
#                     if interval[0]==prevint[1]: twoNums[i][0]=interval[0]
#                     else: 
#                     if interval[1]==nextint[0]: 
#                         twoNums[i][1]=interval[1]
#                         twoNums[i+1][0]=nextint[0]
#                     else: twoNums[i][0]=interval[0]

# from typing import List
# class Solution:
#     def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
#         intervals.sort(key=lambda x: (x[1], -x[0]))
#         res = []
#         for interval in intervals:
#             start, end = interval
#             count = 0
#             for point in reversed(res):
#                 if start <= point <= end: count += 1
#                 if count == 2: break
#             for point in range(end - (1 if count == 1 else 0), end + 1):
#                 if point not in res: res.append(point)
#                 if len(res) >= 2 and all(start <= x <= end for x in res[-2:]): break
#         return len(res)

# from typing import List
# class Solution:
#     def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
#         intervals.sort(key=lambda x: (x[1], -x[0]))
#         res = []
#         for interval in intervals:
#             start, end = interval
#             needed = 2 - sum(start <= p <= end for p in res)
#             for i in range(end, start - 1, -1):
#                 if needed == 0: break
#                 if i not in res:
#                     res.append(i)
#                     needed -= 1
#         return len(res)

from typing import List
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        size = 0
        prev_start = -1
        prev_end = -1
        for curr_start, curr_end in intervals:
            if prev_start == -1 or prev_end < curr_start:
                size += 2
                prev_start = curr_end-1
                prev_end = curr_end
            elif prev_start < curr_start:
                if prev_end != curr_end:
                    prev_start = prev_end
                    prev_end = curr_end
                else:
                    prev_start = curr_end-1
                    prev_end = curr_end
                size += 1
        return size