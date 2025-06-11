# from typing import List
# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         N,D=0,len(arr)-1
#         k-=1
#         currFrac=[arr[N], arr[D]]
#         while k:
#             poss1,poss2=[1,1], [1,1]
#             if N<len(arr): poss1=[arr[N+1], arr[D]]
#             if D>0: poss2=[arr[N], arr[D-1]]
#             if poss1[0]/poss1[1]<poss2[0]/poss2[1]: 
#                 N+=1
#                 k-=1
#                 currFrac=poss1
#             else: 
#                 D-=1
#                 k-=1
#                 currFrac=poss2
#         return currFrac

import heapq
from typing import List
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        # (frac, numIdx, denIdx)
        heap = []
        for j in range(1, n):
            heapq.heappush(heap, (arr[0]/arr[j], 0, j))
        for _ in range(k - 1):
            frac, i, j = heapq.heappop(heap)
            if i + 1 < j: heapq.heappush(heap, (arr[i+1]/arr[j], i+1, j))
        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]