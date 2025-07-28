from typing import List
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        count = 0
        def dfs(index: int, curr_or: int):
            nonlocal max_or, count
            if index == len(nums):
                if curr_or > max_or:
                    max_or = curr_or
                    count = 1
                elif curr_or == max_or: count += 1
                return
            dfs(index + 1, curr_or | nums[index])
            dfs(index + 1, curr_or)
        dfs(0, 0)
        return count