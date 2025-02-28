# from typing import List
# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         i, j = 0, 0
#         res = [[nums1[i], nums2[j]]]
#         while len(res) < k:
#             if i + 1 < len(nums1): temp1 = [nums1[i + 1], nums2[j]]  
#             else: temp1 = None  
#             if j + 1 < len(nums2): temp2 = [nums1[i], nums2[j + 1]]  
#             else: temp2 = None
#             if temp1 and temp2:
#                 if sum(temp1) < sum(temp2):
#                     res.append(temp1)
#                     i += 1
#                 else:
#                     res.append(temp2)
#                     j += 1
#             elif temp1:
#                 res.append(temp1)
#                 i += 1
#             elif temp2:
#                 res.append(temp2)
#                 j += 1
#             else: break
#         return res

from typing import List
from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        heap = []
        res = []
        for i in range(min(k, len(nums1))):  
            heappush(heap, (nums1[i] + nums2[0], i, 0))  
        while heap and len(res) < k:
            s, i, j = heappop(heap)  
            res.append([nums1[i], nums2[j]])  
            if j + 1 < len(nums2): heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res