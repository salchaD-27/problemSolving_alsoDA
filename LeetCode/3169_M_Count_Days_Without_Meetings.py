# from typing import List
# class Solution:
#     def countDays(self, days: int, meetings: List[List[int]]) -> int:
#         def mergeOverlaps(meetings):
#             meetings.sort()
#             for i in range(len(meetings)-1):
#                 if(meetings[i][1]>=meetings[i+1][0]): meetings=meetings[:i]+[meetings[i][0], meetings[i+1][1]]+ meetings[i+2:]
#         mergeOverlaps(meetings)
#         for i in range(len(meetings)):
#             days-=meetings[i][1]-meetings[i][0]+1
#         return days if days>=0 else 0

from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev_end = 0
        for start, end in meetings:
            start = max(start, prev_end + 1)
            length = end - start + 1
            days -= max(length,0)
            prev_end = max(prev_end, end)
        return days