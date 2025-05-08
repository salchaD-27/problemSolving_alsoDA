# from typing import List
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         lastCountMap={}
#         i=interval=0
#         while tasks:
#             if(tasks[i] not in lastCountMap):
#                 lastCountMap[tasks[i]]=interval
#                 tasks.remove(tasks[i])
#                 interval+=1
#                 i=(i+1)%len(tasks)
#             else:
#                 if(interval-lastCountMap[tasks[i]]>n):
#                     lastCountMap[tasks[i]]=interval
#                     tasks.remove(tasks[i])
#                     interval+=1
#                     i=(i+1)%len(tasks)
#                 else: i=(i+1)%len(tasks)
#         return interval+1

import heapq
from typing import List
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)
        time = 0
        cooldown = deque()
        while max_heap or cooldown:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0: cooldown.append((time + n, cnt))
            if cooldown and cooldown[0][0] == time: heapq.heappush(max_heap, cooldown.popleft()[1])
        return time