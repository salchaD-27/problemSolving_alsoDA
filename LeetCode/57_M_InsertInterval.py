# from typing import List
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         startingIntervalIndex = -1
#         start = newInterval[0]
#         for i in range(len(intervals)):
#             if intervals[i][0] <= newInterval[0] <= intervals[i][1]: 
#                 startingIntervalIndex = i
#                 start = min(intervals[i][0], newInterval[0])
#                 break
#         endingIntervalIndex = -1
#         end = newInterval[1]
#         for i in range(len(intervals)):
#             if intervals[i][0] <= newInterval[1] <= intervals[i][1]: 
#                 endingIntervalIndex = i
#                 end = max(intervals[i][1], newInterval[1])
#                 break
#         ans = []
#         for i in range(len(intervals)):
#             if i < startingIntervalIndex or i > endingIntervalIndex: ans.append(intervals[i])
#         ans.append([start, end])
#         return sorted(ans)

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for interval in intervals:
            if newInterval[1] < interval[0]:
                ans.append(newInterval)
                newInterval = interval
            elif newInterval[0] > interval[1]: ans.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        ans.append(newInterval)
        return ans