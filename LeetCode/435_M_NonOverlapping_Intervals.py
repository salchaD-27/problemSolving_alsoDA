from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = float('-inf')
        for interval in intervals:
            if interval[0] < end: count += 1
            else: end = interval[1]
        return count