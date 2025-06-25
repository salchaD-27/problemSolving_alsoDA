# from typing import List
# class Solution:
#     def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
#         i = 0
#         newS = ''
#         idx_map = {idx: pos for pos, idx in enumerate(indices)}
#         while i < len(s):
#             if i in idx_map:
#                 pos = idx_map[i]
#                 src = sources[pos]
#                 tgt = targets[pos]
#                 if s[i:i + len(src)] == src:
#                     newS += tgt
#                     i += len(src)
#                     continue
#             newS += s[i]
#             i += 1
#         return newS
    
from typing import List
class Solution:
    def findReplaceString(self, s, indices, sources, targets):
        patch = {}
        for i, src, tgt in zip(indices, sources, targets):
            if s[i:i+len(src)] == src:
                patch[i] = (src, tgt)
        res, i, n = [], 0, len(s)
        while i < n:
            if i in patch:
                src, tgt = patch[i]
                res.append(tgt)
                i += len(src)
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)