from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        repeated = -1
        n = len(grid)
        for row in grid:
            for num in row:
                if num in seen: repeated = num
                seen.add(num)
        total_numbers = set(range(1, n * n + 1))
        missing = (total_numbers - seen).pop()
        return [repeated, missing]
    
from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        univ=[i for i in range(1, len(grid)**2+1)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in univ: univ.remove(grid[i][j])
                else: univ.insert(0, grid[i][j])
        return univ