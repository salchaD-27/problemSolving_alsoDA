# from typing import List
# class Solution:
#     def pyramidHeights(self, width):
#         heights=[]
#         while(width>1):
#             heights.append(width)
#             width-=2
#         return heights

#     def pyramid(self, grid, i, j, base):
#         if(grid[i][j]==1 and grid[i+1][j-1]==1 and grid[i+1][j]==1 and grid[i+1][j+1]==1 and base==2): return True
#         for a in range(base):
#             for b in range(-a, a+1):
#                 return self.pyramid(grid, i+a, j+b, 2)

#     def ipyramid(self, grid, i, j, base):
#         if(grid[i][j]==1 and grid[i-1][j-1]==1 and grid[i-1][j]==1 and grid[i-1][j+1]==1 and base==2): return True
#         for a in range(base):
#             for b in range(-a, a+1):
#                 return self.pyramid(grid, i-a, j+b, 2)

#     def countPyramids(self, grid: List[List[int]]) -> int:
#         count = 0
#         heights=self.pyramidHeights(len(grid[0]))
#         for base in heights:
#             for i in range(len(grid)):
#                 for j in range(len(grid[0])):
#                     if self.pyramid(grid, i, j, base): count += 1
#                     if self.ipyramid(grid, i, j, base): count += 1
#         return count
    

from typing import List

class Solution:
    def pyramidHeights(self, m, n, grid):
        max_pyramid_heights = [[0] * n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == m-1: max_pyramid_heights[i][j] = 1
                    else:
                        max_pyramid_heights[i][j] = 1 + min(
                            max_pyramid_heights[i + 1][j - 1] if j - 1 >= 0 else 0,
                            max_pyramid_heights[i + 1][j],
                            max_pyramid_heights[i + 1][j + 1] if j + 1 < n else 0
                        )
        return max_pyramid_heights

    def inversePyramidHeights(self, m, n, grid):
        max_inverse_pyramid_heights = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0: max_inverse_pyramid_heights[i][j] = 1
                    else:
                        max_inverse_pyramid_heights[i][j] = 1 + min(
                            max_inverse_pyramid_heights[i - 1][j - 1] if j - 1 >= 0 else 0,
                            max_inverse_pyramid_heights[i - 1][j],
                            max_inverse_pyramid_heights[i - 1][j + 1] if j + 1 < n else 0
                        )
        return max_inverse_pyramid_heights
    
    def countPyramids(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        pyramid_heights = self.pyramidHeights(m, n, grid)
        inverse_pyramid_heights = self.inversePyramidHeights(m, n, grid)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if pyramid_heights[i][j] >= 2: count += pyramid_heights[i][j] - 1
                if inverse_pyramid_heights[i][j] >= 2: count += inverse_pyramid_heights[i][j] - 1
        return count