# from typing import List
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
#         rowPtrs = [0]*n
#         res = []
#         while len(res) < k:
#             minValue = float('inf')
#             minIndex = -1
#             for i in range(n):
#                 if rowPtrs[i] < len(matrix[i]) and matrix[i][rowPtrs[i]] < minValue:
#                     minValue = matrix[i][rowPtrs[i]]
#                     minIndex = i
#             res.append(minValue)
#             rowPtrs[minIndex] += 1
#         return res[-1]

from typing import List
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        minHeap = []
        for i in range(min(k, n)):
            heapq.heappush(minHeap, (matrix[i][0], i, 0))  # (value, row, col)
        for _ in range(k):
            value, r, c = heapq.heappop(minHeap)
            if c + 1 < n: heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        return value