# from typing import List
# class Solution:
#     def maxDistance(self, arrays: List[List[int]]) -> int:
#         globalMin1=float('inf')
#         globalMax1=0
#         globalMin2=float('inf')
#         globalMax2=0
#         for arr in arrays:
#             if(arr[0]<globalMin1 and arr[0]<globalMin2 and arr[-1]>globalMax1 and arr[-1]>globalMax2):
#                 globalMin1=arr[0]
#                 globalMax2=arr[-1]
#             else:
#                 globalMin1=min(globalMin1,arr[0])
#                 globalMin2=min(globalMin2,arr[0])
#                 globalMax1=max(globalMax1,arr[-1])
#                 globalMax2=max(globalMax2,arr[-1])
#         return max(abs(globalMax1-globalMin1),abs(globalMax2-globalMin2))

from typing import List
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        result = 0
        for i in range(1, len(arrays)):
            result = max(result, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0]))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return result