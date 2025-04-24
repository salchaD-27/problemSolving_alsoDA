from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int]):
            if len(path) >= 2: res.append(path[:])
            used = set()
            for i in range(start, len(nums)):
                if (not path or nums[i] >= path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return res