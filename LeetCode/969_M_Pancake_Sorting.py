# from typing import List
# from collections import deque
# class Solution:
#     def pancakeSort(self, arr: List[int]) -> List[int]:
#         def flipped(arr, idx): return arr[:idx][::-1] + arr[idx:]
        
#         target=sorted(arr)
#         queue=deque()
#         for i in range(len(arr)):
#             queue.append([flipped(arr, i), [i]])
#         while queue:
#             tempArr, flips = queue.popleft()
#             if tempArr==target: return flips
#             for i in range(len(arr)):
#                 queue.append([flipped(tempArr, i), flips+[i]])

from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for n in range(len(arr), 1, -1):
            i = arr.index(n)
            if n == i + 1: continue
            if i != 0: res.append(i+1)
            res.append(n) 
            arr[:i+1] = reversed(arr[:i+1])
            arr[:n] = reversed(arr[:n])
        return res