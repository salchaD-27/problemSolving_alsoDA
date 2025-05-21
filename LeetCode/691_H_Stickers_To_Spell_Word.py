from typing import List
from collections import Counter
from functools import lru_cache
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(stickers)
        stickerCounts = [Counter(sticker) for sticker in stickers]
        @lru_cache(None)
        def dfs(remain: str) -> int:
            if not remain: return 0
            remainCount = Counter(remain)
            res = float('inf')
            for sc in stickerCounts:
                if remain[0] not in sc: continue
                newRemain = ""
                for ch in remainCount:
                    if remainCount[ch] > sc.get(ch, 0):
                        newRemain += (ch * (remainCount[ch] - sc.get(ch, 0)))
                used = dfs(newRemain)
                if used != -1: res = min(res, 1 + used)
            return res if res != float('inf') else -1
        return dfs(target)