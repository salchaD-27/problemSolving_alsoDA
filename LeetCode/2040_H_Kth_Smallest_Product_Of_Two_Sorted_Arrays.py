# from typing import List
# class Solution:
#     def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
#         remIdxs={i:[j for j in range(len(nums2))] for i in range(len(nums1))}
#         lastK=-1
#         while k:
#             addedIdx,minIdx,minVal=-1,-1,float('inf')
#             for i in range(len(nums1)):
#                 if len(remIdxs[i])>=1:
#                     if nums1[1]>=0:
#                         prod=nums1[i]*nums2[remIdxs[i][0]]
#                         if prod<minVal:
#                             minVal=prod
#                             minIdx=i
#                             addedIdx=0
#                     else:
#                         prod=nums1[i]*nums2[remIdxs[i][-1]]
#                         if prod<minVal:
#                             minVal=prod
#                             minIdx=i
#                             addedIdx=-1
#             remIdxs[minIdx].pop(addedIdx)
#             lastK=minVal
#             k-=1
#         return lastK
    
# import bisect
# from typing import List
# class Solution:
#     def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
#         def countLessEqual(x):
#             count = 0
#             for a in nums1:
#                 if a > 0: count += bisect.bisect_right(nums2, x // a)
#                 elif a < 0: count += len(nums2) - bisect.bisect_left(nums2, (x + (-1 if x % a else 0)) // a)
#                 elif a == 0 and x >= 0: count += len(nums2)
#             return count
        
#         left = -10**10
#         right = 10**10
#         while left < right:
#             mid = (left + right) // 2
#             if countLessEqual(mid) < k: left = mid + 1
#             else: right = mid
#         return left

import bisect
from typing import List
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_pairs(x: int) -> int:
            count = 0
            for a in nums1:
                if a > 0: count += bisect.bisect_right(nums2, x // a)
                elif a < 0:
                    target = x // a
                    if x % a != 0: target += 1
                    count += len(nums2) - bisect.bisect_left(nums2, target)
                else:
                    if x >= 0: count += len(nums2)
            return count

        low = -10**10
        high = 10**10
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) < k: low = mid + 1
            else: high = mid
        return low