# from collections import defaultdict
# from typing import List
# class Solution:
#     def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
#         allowed_map = defaultdict(list)
#         for rule in allowed:
#             allowed_map[rule[:2]].append(rule[2])

#         def can_build(curr: str) -> bool:
#             if len(curr) == 1: return True
#             def dfs(i: int, path: str) -> bool:
#                 if i == len(curr) - 1: return can_build(path)
#                 pair = curr[i:i+2]
#                 if pair not in allowed_map: return False
#                 for ch in allowed_map[pair]:
#                     if dfs(i + 1, path + ch): return True
#                 return False
#             return dfs(0, "")
        
#         return can_build(bottom)

from collections import defaultdict
from functools import lru_cache
from typing import List
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_map = defaultdict(list)
        for rule in allowed:
            allowed_map[rule[:2]].append(rule[2])
        @lru_cache(None)
        def can_build(curr: str) -> bool:
            if len(curr) == 1: return True
            def dfs(i: int, path: str) -> bool:
                if i == len(curr) - 1: return can_build(path)
                pair = curr[i:i+2]
                if pair not in allowed_map: return False
                for ch in allowed_map[pair]:
                    if dfs(i + 1, path + ch): return True
                return False
            return dfs(0, "")
        return can_build(bottom)