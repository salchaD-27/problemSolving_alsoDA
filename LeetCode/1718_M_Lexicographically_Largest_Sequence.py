#   1
#     2 _ 2
# 3 _ _ 3
# 3,1,2,3,2 (2*3-1=5)

#             1
#   2 _ 2
#     3 _ _ 3
# 4 _ _ _ 4
# 4 2 3 2 4 3 1 (2*4-1=7)

#     1
#             2 _ 2
#   3 _ _ 3
#       4 _ _ _ 4
# 5 _ _ _ _ 5
# 5,3,1,4,3,5,2,4,2 (2*5-1=9)

from typing import List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def backtrack(i: int) -> bool:
            if i == len(res): return True
            if res[i] != 0: return backtrack(i + 1)
            for num in range(n, 0, -1):
                if num in used: continue
                if num > 1 and (i + num >= len(res) or res[i + num] != 0): continue
                used.add(num)
                res[i] = num
                if num > 1: res[i + num] = num
                if backtrack(i + 1): return True
                used.remove(num)
                res[i] = 0
                if num > 1: res[i + num] = 0
            return False

        res = [0] * (2 * n - 1)
        used = set() 
        backtrack(0)
        return res