from typing import List
class Solution:
    def canReach(self, nums: List[int], start: int) -> bool:
        def dfs(i):
            if not(0 <= i < len(nums)) or nums[i] == -1: return False
            if not nums[i]: return True
            temp = nums[i]
            nums[i] = -1
            return dfs(i + temp) or dfs(i - temp)
        return dfs(start)