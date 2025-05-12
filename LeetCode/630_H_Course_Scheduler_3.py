# from typing import List
# class Solution:
#     def scheduleCourse(self, courses: List[List[int]]) -> int:
#         def branch(currCount, currDays, remCourses):
#             if not remCourses: return currCount
#             max_count = currCount
#             for i in range(len(remCourses)):
#                 duration, lastDay = remCourses[i]
#                 remaining = remCourses[:i] + remCourses[i+1:]
#                 # with the course
#                 if currDays + duration <= lastDay: max_count = max(max_count, branch(currCount + 1, currDays + duration, remaining))
#                 # without the course
#                 max_count = max(max_count, branch(currCount, currDays, remaining))
#             return max_count
#         return branch(0, 0, courses)
    
import heapq
from typing import List
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        total_time = 0
        max_heap = []
        for duration, lastDay in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)
            if total_time > lastDay:
                longest = -heapq.heappop(max_heap)
                total_time -= longest
        return len(max_heap)