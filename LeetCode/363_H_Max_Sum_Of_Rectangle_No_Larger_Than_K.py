# from typing import List
# class Solution:
#     def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
#         def rectanglify(row, k):
#             ans = float('-inf')
#             for i in range(len(row)):
#                 sum_subarray = 0
#                 for j in range(i, len(row)):
#                     sum_subarray += row[j]
#                     if sum_subarray <= k: ans = max(ans, sum_subarray)
#             return ans
        
#         ans = float('-inf')
#         for i in range(len(matrix)):
#             for j in range(1, len(matrix[i])):
#                 matrix[i][j] += matrix[i][j - 1]
#         for i in range(1, len(matrix)):
#             for j in range(len(matrix[i])):
#                 matrix[i][j] += matrix[i - 1][j]
#         for row in matrix:
#             ans = max(ans, rectanglify(row, k))
#         return ans

from typing import List
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        for top in range(rows):
            row_sums = [0] * cols
            for bottom in range(top, rows):
                for col in range(cols):
                    row_sums[col] += matrix[bottom][col]
                max_subarray_sum = self.maxSubarraySumNoLargerThanK(row_sums, k)
                max_sum = max(max_sum, max_subarray_sum)
                if max_sum == k: return k
        return max_sum

    def maxSubarraySumNoLargerThanK(self, arr: List[int], k: int) -> int:
        max_sum = float('-inf')
        prefix_sum = 0
        prefix_sums = [0]
        for num in arr:
            prefix_sum += num
            idx = bisect.bisect_left(prefix_sums, prefix_sum - k)
            if idx < len(prefix_sums): max_sum = max(max_sum, prefix_sum - prefix_sums[idx])
            bisect.insort(prefix_sums, prefix_sum)
        return max_sum