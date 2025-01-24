from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def combine(nums, k):
            def backtrack(start, combination):
                if len(combination) == k:
                    result.append(combination[:]) 
                    return
                for i in range(start, len(nums)):
                    combination.append(nums[i]) 
                    backtrack(i + 1, combination)
                    combination.pop() 
            result = []
            backtrack(0, [])
            return result
        ans = [[]] 
        for i in range(1, len(nums) + 1): 
            ans.extend(combine(nums, i))
        return ans