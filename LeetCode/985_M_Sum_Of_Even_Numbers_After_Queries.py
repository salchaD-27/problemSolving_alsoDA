from typing import List
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        mp = {i: val for i, val in enumerate(nums)}
        c = sum(val for val in nums if val % 2 == 0)
        ans = []
        for v, idx in queries:
            mpv = mp[idx]
            if mpv % 2 == 0: c -= mpv
            mpv += v
            mp[idx] = mpv
            if mpv % 2 == 0: c += mpv
            ans.append(c)
        return ans