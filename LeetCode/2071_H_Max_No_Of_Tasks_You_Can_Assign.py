# from typing import List
# class Solution:
#     def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
#         tasks.sort(reverse=True)
#         workers.sort(reverse=True)
#         workerIdx=0
#         count=0
#         for i in range(len(tasks)):
#             if(workers[workerIdx]>=tasks[i]):
#                 count+=1
#                 workerIdx+=1
#             else:
#                 if(pills and workers[workerIdx]+strength>=tasks[i]):
#                     count+=1
#                     workerIdx+=1
#                     pills-=1
#                 else:
#                     continue
#         return count

# from typing import List
# from collections import deque
# class Solution:
#     def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
#         tasks.sort()
#         workers.sort()

#         def can_assign(k):
#             task_deque = deque(tasks[:k])
#             available_workers = workers[-k:]
#             pills_left = pills
#             for i in range(k - 1, -1, -1): 
#                 if not task_deque: break
#                 if available_workers[i] >= task_deque[-1]: task_deque.pop()
#                 elif pills_left and available_workers[i] + strength >= task_deque[0]: 
#                     task_deque.popleft()
#                     pills_left -= 1
#                 else: return False
#             return not task_deque 

#         low, high = 0, min(len(tasks), len(workers))
#         answer = 0
#         while low <= high:
#             mid = (low + high) // 2
#             if can_assign(mid):
#                 answer = mid
#                 low = mid + 1
#             else: high = mid - 1
#         return answer

# from typing import List
# class Solution:
#     def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
#         def getIdx(remWorkers, remTasks, pillStrength):
#             for i in range(len(remTasks)):
#                 last_valid = -1
#                 for j in range(len(remWorkers)):
#                     if remWorkers[j] + pillStrength >= remTasks[i]: last_valid = j
#                     else: break
#                 if last_valid != -1: return last_valid, i
#             return -1, -1

#         tasks.sort(reverse=True)
#         workers.sort(reverse=True)
#         count = 0
#         while pills:
#             workIdx, taskIdx = getIdx(workers, tasks, strength)
#             if workIdx == -1: break
#             del workers[workIdx]
#             del tasks[taskIdx]
#             pills -= 1
#             count += 1
#         workerIdx = 0
#         for i in range(len(tasks)):
#             if workerIdx >= len(workers): break
#             if workers[workerIdx] >= tasks[i]:
#                 count += 1
#                 workerIdx += 1
#         return count

from typing import List
from collections import deque
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def can_finish(mid, pills):
            n = len(workers)
            i = 0
            queue = deque()
            for j in range(n - mid, n):
                w = workers[j]
                while i < mid and tasks[i] <= w + strength:
                    queue.append(tasks[i])
                    i += 1
                if not queue: return False
                if queue[0] <= w: queue.popleft()
                else: 
                    if pills == 0: return False
                    pills -= 1
                    queue.pop()
            return True
        
        left = 0
        right = min(len(tasks), len(workers))
        while left< right:
            mid = (left + right+1)// 2
            if can_finish(mid, pills): left = mid
            else: right = mid - 1
        return left