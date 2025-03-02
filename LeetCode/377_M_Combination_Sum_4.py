from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def backtrack(remTarget):
            if remTarget == 0: return 1
            if remTarget in memo: return memo[remTarget]
            count = 0
            for num in nums:
                if remTarget >= num: count += backtrack(remTarget - num)
            memo[remTarget] = count
            return count

        memo = {}
        return backtrack(target)