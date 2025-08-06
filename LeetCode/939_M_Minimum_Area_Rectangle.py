import sys
from typing import List
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        ans = sys.maxsize
        for x1, y1 in points:
            for x2, y2 in points:
                if (x1,y2) in seen and (x2,y1) in seen: ans = min(ans, abs((x2-x1)*(y2-y1)))
            seen.add((x1,y1))
        return ans if ans != sys.maxsize else 0

from collections import defaultdict
class Solution(object):
    def minAreaRect(self, points):
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')
        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx: ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0