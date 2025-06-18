# from typing import List
# class Solution:
#     def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
#         nums.sort()
#         res=[[nums[0]]]
#         for i in range(1, len(nums)):
#             added=False
#             for j in range(len(res)):
#                 if len(res[j])<3 and abs(max(res[j])-nums[i])<=k and abs(min(res[j])-nums[i])<=k:
#                     res[j].append(nums[i])
#                     added=True
#             if not added: res.append([nums[i]])
#         for arr in res:
#             if len(arr)!=3: return []
#         return res

from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            if i + 2 >= len(nums): return []
            group = nums[i:i+3]
            if group[2] - group[0] > k: return []
            res.append(group)
        return res