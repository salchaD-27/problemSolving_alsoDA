from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or heights[r][c] < prevHeight): return
            visit.add((r, c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, heights[r][c])

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) 
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])  
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) 
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) 
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res