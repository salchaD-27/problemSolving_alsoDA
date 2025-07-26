# from typing import List
# from collections import defaultdict
# class Solution:
#     def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
#         all_nums = list(range(1, n + 1))
#         # total = n * (n + 1) // 2        
#         max_subarrays = 0
#         for idx in range(len(conflictingPairs)):
#             conflicts = set()
#             for i, (a, b) in enumerate(conflictingPairs):
#                 if i != idx:
#                     conflicts.add((a, b))
#                     conflicts.add((b, a))
#             left = 0
#             count = 0
#             pos = {}
#             for right in range(n):
#                 num = all_nums[right]
#                 pos[num] = right
#                 while any((all_nums[i], num) in conflicts for i in range(left, right)):
#                     left += 1
#                 count += right - left + 1
#             max_subarrays = max(max_subarrays, count)
#         return max_subarrays

from typing import List
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        ans = 0 
        left = [0, 0] 
        bonus = [0] * (n + 1)
        for r in range(1, n + 1):
            for l in right[r]:
                if l > left[0]: left = [l, left[0]]
                elif l > left[1]: left = [left[0], l]
            ans += r - left[0]
            if left[0] > 0: bonus[left[0]] += left[0] - left[1]
        return ans + max(bonus)