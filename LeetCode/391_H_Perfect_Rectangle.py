from typing import List
class Solution:                
    def largestRectangleDimensions(self, heights):
        stack = []
        max_height = 0
        max_width = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height_index = stack.pop()
                height = heights[height_index]
                width = i if not stack else i - stack[-1] - 1
                if height * width > max_height * max_width: max_height, max_width = height, width
            stack.append(i)
        return max_height, max_width
    
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]: return 0, 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_height = 0
        max_width = 0
        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == 1 else 0 
            height, width = self.largestRectangleDimensions(heights)
            if height * width > max_height * max_width:
                max_height, max_width = height, width
        return max_height, max_width
    
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        def fillGrid(dimensions, grid, minX, minY):
            x, y, a, b = dimensions
            for i in range(y - minY, b - minY):
                for j in range(x - minX, a - minX):
                    if grid[i][j] == 1: return False
                    grid[i][j] = 1
            return True
        minX = min(x for x, y, a, b in rectangles)
        minY = min(y for x, y, a, b in rectangles)
        maxA = max(a for x, y, a, b in rectangles)
        maxB = max(b for x, y, a, b in rectangles)
        grid = [[0] * (maxA - minX) for _ in range(maxB - minY)]
        for rect in rectangles:
            if not fillGrid(rect, grid, minX, minY): return False
        return self.maximalRectangle(grid) == (maxB - minY, maxA - minX)






from typing import List
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area_sum = 0
        point_set = set()
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
        for x1, y1, x2, y2 in rectangles:
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)
            area_sum += (x2 - x1) * (y2 - y1)
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in point_set: point_set.remove(point)
                else: point_set.add(point)
        expected_area = (max_x - min_x) * (max_y - min_y)
        if area_sum != expected_area: return False
        expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        return point_set == expected_corners