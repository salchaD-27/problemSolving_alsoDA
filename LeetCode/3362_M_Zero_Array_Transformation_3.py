# from typing import List
# class Solution:
#     def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
#         def isZeroArray(nums, queries):
#             diff = [0]*(len(nums) + 1)
#             for l, r in queries:
#                 diff[l] += 1
#                 if r + 1 < len(nums): diff[r + 1] -= 1
#             cnt = 0
#             for i in range(len(nums)):
#                 cnt += diff[i]
#                 if nums[i] > cnt: return False
#             return True
        
#         if not isZeroArray(nums, queries): return -1
#         count=0
#         for i in range(len(queries)):
#             if isZeroArray(nums, queries[:i]+queries[i+1:]): count+=1
#         return count

# from typing import List
# from itertools import combinations
# class Solution:
#     def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
#         def isZeroArray(nums, queries):
#             diff = [0] * (len(nums) + 1)
#             for l, r in queries:
#                 diff[l] += 1
#                 if r + 1 < len(nums):
#                     diff[r + 1] -= 1
#             cnt = 0
#             for i in range(len(nums)):
#                 cnt += diff[i]
#                 if nums[i] > cnt: return False
#             return True

#         if not isZeroArray(nums, queries): return -1
#         max_removal = 0
#         n = len(queries)
#         for remove_count in range(1, n + 1):
#             for remove_indices in combinations(range(n), remove_count):
#                 remaining_queries = [q for i, q in enumerate(queries) if i not in remove_indices]
#                 if isZeroArray(nums, remaining_queries): max_removal = max(max_removal, remove_count)
#         return max_removal

# from typing import List
# class Solution:
#     def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
#         def isZeroArray(nums, queries):
#             diff = [0] * (len(nums) + 1)
#             for l, r in queries:
#                 diff[l] += 1
#                 if r + 1 < len(nums): diff[r + 1] -= 1
#             cnt = 0
#             for i in range(len(nums)):
#                 cnt += diff[i]
#                 if nums[i] > cnt: return False
#             return True

#         if not isZeroArray(nums, queries): return -1
#         left, right = 0, len(queries)
#         result = 0
#         while left <= right:
#             mid = (left + right) // 2
#             found = False
#             for i in range(len(queries) - mid + 1):
#                 to_remove = set(range(i, i + mid))
#                 remaining_queries = [q for j, q in enumerate(queries) if j not in to_remove]
#                 if isZeroArray(nums, remaining_queries):
#                     found = True
#                     break
#             if found:
#                 result = mid
#                 left = mid + 1
#             else: right = mid - 1
#         return result

import heapq
from typing import List
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)
        starts = [[] for _ in range(n)]
        for l, r in queries:
            starts[l].append(r)
        avail = []
        active = []
        chosen = 0
        for i in range(n):
            for r in starts[i]:
                heapq.heappush(avail, -r)
            while active and active[0] < i:
                heapq.heappop(active)
            need = nums[i] - len(active)
            for _ in range(need):
                while avail and -avail[0] < i:
                    heapq.heappop(avail)
                if not avail:
                    return -1
                r = -heapq.heappop(avail)
                heapq.heappush(active, r)
                chosen += 1
        return q - chosen