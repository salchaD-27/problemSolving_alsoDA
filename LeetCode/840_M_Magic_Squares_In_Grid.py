from typing import List
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i, j):
            nums = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if sorted(nums) != list(range(1, 10)): return False
            for x in range(3):
                if sum(grid[i+x][j:j+3]) != 15: return False
            for y in range(3):
                if grid[i][j+y] + grid[i+1][j+y] + grid[i+2][j+y] != 15: return False
            if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != 15: return False
            if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != 15: return False
            return True

        rows, cols = len(grid), len(grid[0])
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j): count += 1
        return count