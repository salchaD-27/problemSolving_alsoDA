from typing import List
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        s = set(map(tuple,queens))
        ans = []
        x0, y0 = king
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
            x, y = x0+dx, y0+dy
            while 0 <= x < 8 and 0 <= y < 8:
                if (x,y) in s:
                    ans.append([x,y])
                    break
                x += dx
                y += dy
        return ans