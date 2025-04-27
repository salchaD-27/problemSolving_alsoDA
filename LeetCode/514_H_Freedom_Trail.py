# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
#         def distFromLeft(ring, initialI, keyChar):
#             n = len(ring)
#             i = (initialI + 1) % n
#             dist = 1
#             while ring[i] != keyChar:
#                 i = (i + 1) % n
#                 dist += 1
#             return dist

#         def distFromRight(ring, initialI, keyChar):
#             n = len(ring)
#             i = (initialI - 1 + n) % n
#             dist = 1
#             while ring[i] != keyChar:
#                 i = (i - 1 + n) % n
#                 dist += 1
#             return dist

#         n = len(ring)
#         i = 0
#         keyI = 0
#         cost = 0
#         while keyI < len(key):
#             if ring[i] == key[keyI]:
#                 cost += 1
#             else:
#                 left = distFromLeft(ring, i, key[keyI])
#                 right = distFromRight(ring, i, key[keyI])
#                 if left < right:
#                     cost += left + 1
#                     i = (i + left) % n
#                 else:
#                     cost += right + 1
#                     i = (i - right + n) % n
#             keyI += 1
#         return cost

from functools import lru_cache
from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        char_to_indices = defaultdict(list)
        for i, ch in enumerate(ring):
            char_to_indices[ch].append(i)

        @lru_cache(None)
        def dp(pos: int, key_index: int) -> int:
            if key_index == len(key): return 0
            res = float('inf')
            target_char = key[key_index]
            for i in char_to_indices[target_char]:
                diff = abs(pos - i)
                step = min(diff, n - diff)
                res = min(res, step + 1 + dp(i, key_index + 1))
            return res
        return dp(0, 0)