# 1 2 3 4 3
# 1 2 3 4
# 2 3 4 -1

# 1 2 3 4 3
# 2 3 4 -1 3
    
# from typing import List
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         orderedNums = sorted(set(nums))
#         nGE = {orderedNums[i]: orderedNums[i+1] if i+1 < len(orderedNums) else -1 for i in range(len(orderedNums))}
#         return [nGE[num] for num in nums]

from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            curr = nums[i % n]
            while stack and nums[stack[-1]] < curr:
                idx = stack.pop()
                res[idx] = curr
            if i < n: stack.append(i)
        return res