import bisect
from typing import List
from functools import lru_cache
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        start_days = [event[0] for event in events]
        n = len(events)
        @lru_cache(None)
        def dp(i, count):
            if i == n or count == 0: return 0
            res = dp(i + 1, count) # skipping this event
            _, end, value = events[i] # taking this event
            next_i = bisect.bisect_right(start_days, end) # nxt nonoverlapping event
            res = max(res, value + dp(next_i, count - 1))
            return res
        return dp(0, k)