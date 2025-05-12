# [4,10,15,24,26], [0,9,12,20], [5,18,22,30]
# 4,26 0,20 5,30
# =>5,20
# 5: 
# 20: 20-24

# from typing import List
# class Solution:
#     def smallestRange(self, nums: List[List[int]]) -> List[int]:
#         interval=[float('-inf'),float('inf')]
#         for i in range(len(nums)):
#             interval[0]=max(interval[0], nums[i][0])
#             interval[1]=min(interval[1], nums[i][-1])
#         interval0=[interval[0],interval[0]]
#         interval1=[interval[1],interval[1]]
#         for i in range(len(nums)):
#             for j in range(len(nums[i])):
#                 if nums[i][j]<=interval0[0]: interval0[0]=nums[i][j]
#             for j in reversed(range(len(nums[i]))):
#                 if nums[i][j]>=interval1[1]: interval1[1]=nums[i][j]
#         return interval0 if (interval0[1]-interval0[0] < interval1[1]-interval1[0]) or (interval0[0]<interval1[0]) else interval1

import heapq
from typing import List
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        cur_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0)) 
            cur_max = max(cur_max, nums[i][0])
        small = [float('-inf'), float('inf')]
        while heap:
            cur_min, list_idx, i = heapq.heappop(heap)
            if cur_max - cur_min < small[1] - small[0]: small = [cur_min, cur_max]
            if i + 1 < len(nums[list_idx]):
                nxt = nums[list_idx][i + 1]
                heapq.heappush(heap, (nxt, list_idx, i+1))
                cur_max = max(cur_max, nxt)
            else: break
        return small