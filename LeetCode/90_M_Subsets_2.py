# from typing import List
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         ans=[[]]
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if(nums[i:j+1] not in ans): ans.append(nums[i:j+1])
#         return ans

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        def backtrack(index):
            result.append(subset[:])
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]: continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        backtrack(0)
        return result