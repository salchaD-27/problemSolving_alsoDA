# candidates = [2,3,6,7]
# target = 7
# if to check for 0 in [...], (=base case for recursion) return that num
# if to check for x in [...], and all nums > than x, return cause no sum with such combination possible
# if to check for x in [...], and a num = x, return that num, and it reduces to base case
# check for 7 in [2,3,6,7]=
# [2] + check for 5 in [2,3,6,7]
# [3] + check for 4 in [2,3,6,7]
# [6] + check for 1 in [2,3,6,7]
# [7] + check for 0 in [2,3,6,7]

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > target: continue
                path.append(num)
                backtrack(i, target - num, path)
                path.pop()
        candidates.sort()
        backtrack(0, target, [])
        return result