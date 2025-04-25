# import random
# from typing import List
# class Solution:
#     def __init__(self, rects: List[List[int]]):
#         self.rects = rects
#         self.minX = self.minY = float('inf')
#         self.maxX = self.maxY = float('-inf')
#         for x1, y1, x2, y2 in rects:
#             self.minX = min(self.minX, x1, x2)
#             self.maxX = max(self.maxX, x1, x2)
#             self.minY = min(self.minY, y1, y2)
#             self.maxY = max(self.maxY, y1, y2)
#     def pick(self) -> List[int]:
#         while True:
#             x = random.randint(self.minX, self.maxX)
#             y = random.randint(self.minY, self.maxY)
#             for x1, y1, x2, y2 in self.rects:
#                 left, right = min(x1, x2), max(x1, x2)
#                 bottom, top = min(y1, y2), max(y1, y2)
#                 if left <= x <= right and bottom <= y <= top: return [x, y]

import random
from typing import List
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        total = 0
        for x1, y1, x2, y2 in rects:
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            total += area
            self.weights.append(total)
    def pick(self) -> List[int]:
        target = random.randint(1, self.weights[-1])
        l, r = 0, len(self.weights) - 1
        while l < r:
            mid = (l + r) // 2
            if target <= self.weights[mid]: r = mid
            else: l = mid + 1
        rect = self.rects[l]
        x1, y1, x2, y2 = rect
        return [random.randint(x1, x2), random.randint(y1, y2)]