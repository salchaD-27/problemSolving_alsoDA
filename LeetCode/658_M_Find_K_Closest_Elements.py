# from typing import List
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         res=[]
#         lastDiff=0
#         while k:
#             while(lastDiff-x in arr):
#                 res.append(lastDiff-x)
#                 arr.remove(lastDiff-x)
#                 k-=1
#             lastDiff+=1
#         return res

from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x: left = mid + 1
            else: right = mid
        return arr[left:left + k]